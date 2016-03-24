#include <FaceTracker/Tracker.h>
#include <opencv/highgui.h>
#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <fstream>
#include <iomanip>

using namespace std;

//=============================================================================
CV_INLINE  int  cvRound( float value )
{
#if defined HAVE_LRINT || defined CV_ICC || defined __GNUC__
  return (int)lrint(value);
#else
  // while this is not IEEE754-compliant rounding, it's usually a good enough approximation
  return (int)(value + (value >= 0 ? 0.5f : -0.5f));
#endif
}
//=============================================================================
void Draw(cv::Mat &image,cv::Mat &shape,cv::Mat &con,cv::Mat &tri,cv::Mat &visi, std::string fname)
{
  int i,n = shape.rows/2; cv::Point p1,p2; cv::Scalar c;

  //draw points
  for(i = 0; i < n; i++){    
    if(visi.at<int>(i,0) == 0)continue;
    p1 = cv::Point(shape.at<double>(i,0),shape.at<double>(i+n,0));
    c = CV_RGB(0,255,0); cv::circle(image,p1,2,c);
    //cv::putText(image, std::to_string(i+1),p1,CV_FONT_HERSHEY_PLAIN,0.5,cv::Scalar::all(0));
  }

  //cout<<typeid(shape.at<double>(i,0)).name();
  fstream file;

      file.open(fname+".vector", ios_base::out);
      for(int i = 0; i < n; i++)
          file << std::fixed << std::setprecision(8)<<shape.at<double>(i,0)<<"   "<<shape.at<double>(i+n,0)<<endl;
      file.close();
      return;


  //put to file


}
//=============================================================================
int set_param(char* ftFile,char* conFile,char* triFile,
	      bool &fcheck,double &scale,int &fpd)
{
  fcheck = false; scale = 1; fpd = -1;

  //new assignments
  strcpy(triFile,"model/face.tri");
  strcpy(conFile,"model/face.con");
  strcpy(ftFile,"model/face2.tracker");
  //fcheck = true;
  return 0;
}
//=============================================================================
int main(int argc, char** argv)
{
  //set parameters
  char ftFile[256],conFile[256],triFile[256];
  bool fcheck = false; double scale = 1; int fpd = -1;
  if(set_param(ftFile,conFile,triFile,fcheck,scale,fpd)<0)return 0;
  //set other tracking parameters
  std::vector<int> wSize1(1); wSize1[0] = 7;
  std::vector<int> wSize2(3); wSize2[0] = 11; wSize2[1] = 9; wSize2[2] = 7;
  int nIter = 5; double clamp=3,fTol=0.01; 
  FACETRACKER::Tracker model(ftFile);
  cv::Mat tri=FACETRACKER::IO::LoadTri(triFile);
  cv::Mat con=FACETRACKER::IO::LoadCon(conFile);
  std::string fname(argv[1]);

  cv::Mat tmp,frame,gray,im;


  bool failed = true;
				frame=cv::imread(argv[1],CV_LOAD_IMAGE_COLOR);
				if(scale == 1)im = frame;
				else cv::resize(frame,im,cv::Size(scale*frame.cols,scale*frame.rows));
				cv::cvtColor(im,gray,CV_BGR2GRAY);
				while(fname.back()!='.')
				{
					fname.pop_back();
				}
				fname.pop_back();

//=============	 track this image
				std::vector<int> wSize; if(failed)wSize = wSize2; else wSize = wSize1;
				;
				if(model.Track(gray,wSize,fpd,nIter,clamp,fTol,fcheck) == 0)
				{
				  int idx = model._clm.GetViewIdx(); failed = false;
				  Draw(im,model._shape,con,tri,model._clm._visi[idx],fname);
				}
				else
				{

				  model.FrameReset(); failed = true;
				}

//============ flip image and draw
				cv::flip(frame, frame,1);
				im= frame;
				if(scale == 1)im = frame;
				else cv::resize(frame,im,cv::Size(scale*frame.cols,scale*frame.rows));
				cv::cvtColor(im,gray,CV_BGR2GRAY);


//=============	 track this image
				if(failed)wSize = wSize2; else wSize = wSize1;
				;
				if(model.Track(gray,wSize,fpd,nIter,clamp,fTol,fcheck) == 0)
				{
				  int idx = model._clm.GetViewIdx(); failed = false;
				  fname = fname + "_mirror";
				  Draw(im,model._shape,con,tri,model._clm._visi[idx],fname);
				}
				else
				{

				  model.FrameReset(); failed = true;
				}


  	  	  return 0;
}
//=============================================================================
