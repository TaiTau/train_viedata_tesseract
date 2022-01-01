
import cv2



#############################################################################################


f = open('list.lst', 'rt')
lines = f.readlines()
f.close()
#i_count = 0
for line in lines:

    #i_count = i_count + 1
    line = line.replace('\n', '')
    print(line)
    I = cv2.imread(line)

    cv2.imshow(line + "_huy", I)
    cv2.waitKey(0)
    #szOut = './out/' + line[:len(line) - 4] + '_kieu3' + '.png'
    #cv2.imwrite(szOut, I)
cv2.waitKey()