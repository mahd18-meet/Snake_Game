import turtle
import random
turtle.tracer(1,0)

#Variables
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)
turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

#Lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Setup snake
snake = turtle.clone()
snake.shape('square')
turtle.hideturtle()

def new_stamp():
	snake_pos = snake.pos()
	
	snake_stamp = snake.stamp()
	stamp_list.append(snake_stamp)
	pos_list.insert(-1,snake_pos)


for i in range(START_LENGTH):
	x_pos = snake.pos()[0]
	y_pos = snake.pos()[1]
	x_pos += SQUARE_SIZE
	snake.goto(x_pos, y_pos)
	new_stamp()


def remove_tail():
	old_stamp = stamp_list.pop(0)
	snake.clearstamp(old_stamp)
	pos_list.pop(0)


snake.direction = "Up"

def up():
	snake.direction = "Up"
	
	print("You pressed the up key.")

def down():
	snake.direction = "Down"
	
	print("You pressed the Down key.")

def right():
	snake.direction = "Right"
	
	print("You pressed the right key.")

def left():
	snake.direction = "Left"
	
	print("You pressed the left key.")

turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")	
	
turtle.listen()
turtle.register_shape("small_apple.gif")
food = turtle.clone()
food_pos = []
food_stamps = []
food.hideturtle()
food.shape("small_apple.gif")



def make_food():

	min_x = -int(SIZE_X/2/SQUARE_SIZE) + 1
	max_x = int(SIZE_X/2/SQUARE_SIZE) - 1
	min_y = -int(SIZE_Y/2/SQUARE_SIZE) +1
	max_y = int(SIZE_Y/2/SQUARE_SIZE) -1

	food_x = random.randint(min_x,max_x) * SQUARE_SIZE
	food_y = random.randint(min_y, max_y) * SQUARE_SIZE
	food.goto(food_x,food_y)
	food_pos.append(food.pos())
	new_food_stamp = food.stamp()
	food_stamps.append(new_food_stamp)




def move_snake():
	my_pos = snake.pos()
	x_pos = my_pos[0]
	y_pos = my_pos[1]

	if snake.direction == "Up":
		snake.goto(x_pos, y_pos+SQUARE_SIZE)
		print("Up")
	elif snake.direction == "Down":
		snake.goto(x_pos, y_pos - SQUARE_SIZE)
		print('Down')
	elif snake.direction == "Right":
		snake.goto(x_pos+SQUARE_SIZE, y_pos)
		print('Right')
	else:
		snake.goto(x_pos - SQUARE_SIZE,y_pos)
		print('Left')

	new_stamp()	
	if snake.pos() in food_pos:
		food_index=food_pos.index(snake.pos())
		food.clearstamp(food_stamps[food_index])
		food_pos.pop(food_index)
		food_stamps.pop(food_index)
		print("Eaten food")
		make_food()
		
		
	else:
		remove_tail()
	
	

	new_pos_list = set(pos_list)
	print(new_pos_list,pos_list)
	if len(new_pos_list) != len(pos_list):
		print("Game over!")
		quit()




	#PART 8
	
	#SPECIAL PLACE

	new_pos = snake.pos()
	new_x_pos = new_pos[0]
	new_y_pos = new_pos[1]
	if new_x_pos >= RIGHT_EDGE:
		print("GAME OVER")
		quit()
	elif new_x_pos <= LEFT_EDGE:
		print("GAME OVER")
		quit()
	elif new_y_pos >= UP_EDGE:
		print("GAME OVER")
		quit()
	elif new_y_pos <= DOWN_EDGE:
		print("GAME OVER")
		quit()
	if len(food_stamps) <=1:
		make_food()
	turtle.ontimer(move_snake,TIME_STEP)

move_snake()