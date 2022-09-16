import cv2 as cv
import openpyxl


template_path = "utils\Template.jpg"
details_path = "utils\participants.xlsx"
n = 4   # number of participants in participants.xlsx

output_path = "Certificates"


font_size = 1
font_color = (164,198,57)


coordinate_y_adjustment = 85
coordinate_x_adjustment = 7


obj = openpyxl.load_workbook(details_path)
sheet = obj.active


for i in range(1,n+1):
    

    get_name = sheet.cell(row = i ,column = 1)
    certi_name = get_name.value

    print(certi_name)

                               
    # read the certificate template
    img = cv.imread(template_path)
                                 
    # choose the font from opencv
    font = cv.FONT_HERSHEY_SIMPLEX

    
    text_size = cv.getTextSize(certi_name, font, font_size, 0)[0]     
   
    
    text_x = (img.shape[1] - text_size[0]) / 2 + coordinate_x_adjustment 
    text_y = (img.shape[0] + text_size[1]) / 2 - coordinate_y_adjustment
    text_x = int(text_x)
    text_y = int(text_y)
    cv.putText(img, certi_name,
              (text_x ,text_y ), 
              font,
              font_size,
              font_color, 3)
   
    
    certi_path = f"{output_path}/{certi_name}.jpg"

    print(certi_path)

       
    # Save the certificate                      
    try:
        cv.imwrite(certi_path,img)
    except Exception as e:
        print(e)
        