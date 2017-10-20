import OutputConsole as out
import PIL.Image as pil
def outImages(type):
    if(type == 'test'):
        for i in range(len(out.ReadDataFiles.test_images)):
            myimage = pil.fromarray(out.np.array(out.ReadDataFiles.test_images[i]))
            mylabel = out.ReadDataFiles.test_labels[i]
            # convert image
            myimage = myimage.convert('RGB')
            # save image
            imagename = 'test_images/test-'+str(i)+'-'+str(mylabel)+'.png'
            myimage.save(imagename)
    if(type == 'train'):
        for i in range(len(out.ReadDataFiles.train_images)):
            myimage = pil.fromarray(out.np.array(out.ReadDataFiles.train_images[i]))
            mylabel = out.ReadDataFiles.train_labels[i]
            # convert image
            myimage = myimage.convert('RGB')
            # save image
            imagename = 'train_images/train-'+str(i)+'-'+str(mylabel)+'.png'
            myimage.save(imagename)

outImages('test')
outImages('train')