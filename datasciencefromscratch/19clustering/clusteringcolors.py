path_to_png_file = r"C:\example\path\to\example.png"
import matplotlib.image as mpimg
img = mpimg.imread(path_to_png_file)

top_row = img[0]
top_left_pixel = top_row[0]
red, green, blue = top_left_pixel

pixels = [pixel for row in img for pixel in row]

clusterer = kMeans(5)
clusterer.train(pixels)	# this might take a while

def recolor(pixel):
	cluster = clusterer.classify(pixel)
	return clusterer.means[cluster]

new_img = [[recolor(pixil) for pixel in row]
			for row in img]

plt.imshow(new_img)
plt.axis('off')
plt.show()