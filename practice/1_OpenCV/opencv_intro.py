import argparse
import sys
import cv2


def make_cat_passport_image(input_image_path, haar_model_path):
    image = cv2.imread(input_image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    resized = cv2.resize(gray, (640, 480), interpolation = cv2.INTER_AREA)
    detector = cv2.CascadeClassifier(haar_model_path) 
    rects = detector.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(75, 75))
    #cv2.imshow("window_name", image) 
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
    for (i, (x, y, w, h)) in enumerate(rects):
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    
    x, y, w, h = rects[0] 
    image = image[y:y+h, x:x+w]
    cv2.imwrite("out_cat.jpg", image) 
    image = cv2.imread("out_cat.jpg")
    
    image2 = cv2.imread("pet_passport.png")
    image2[45:45+h,45:45+w] = image
    org = (80,220)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.5
    color = (255, 0, 0)
    thickness = 1
    image2 = cv2.putText(image2,'Pupsik',org,font,fontScale,color,thickness,cv2.LINE_AA)
    cv2.imwrite("out_passport.jpg", image2)
    
    # Read image

    # Convert image to grayscale

    # Normalize image intensity

    # Resize image

    # Detect cat faces using Haar Cascade

    # Draw bounding box

    # Display result image

    # Crop image

    # Save result image to file

    return


def build_argparser():
    parser = argparse.ArgumentParser(
        description='Speech denoising demo', add_help=False)
    args = parser.add_argument_group('Options')
    args.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                      help='Show this help message and exit.')
    args.add_argument('-m', '--model', type=str, required=True,
                      help='Required. Path to .XML file with pre-trained model.')
    args.add_argument('-i', '--input', type=str, required=True,
                      help='Required. Path to input image')
    return parser


def main():
    
    args = build_argparser().parse_args()
    make_cat_passport_image(args.input, args.model)

    return 0


if __name__ == '__main__':
    sys.exit(main() or 0)
