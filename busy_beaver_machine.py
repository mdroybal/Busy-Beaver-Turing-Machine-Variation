import sys

class Busy_Beaver():

	def __init__(self,state="b"):
		self.tape = [0 for i in range(0,56)]
		self.tape_position = 28 #start in the middle of the tape
		self.state = state
		self.end_count = 0
		self.display_info()

	def __str__(self):
		return "{}".format(self.tape)

	def move_left(self):
		self.tape_position+=1

	def move_right(self):
		self.tape_position-=1

	def display_info(self):
		print "state: {} {}".format(self.state,self.tape[self.tape_position-6:self.tape_position+8])

	def state_A(self):
		if self.tape[self.tape_position] == 0:
			self.tape[self.tape_position] = 1
			self.move_right()
			self.state = "B"
			self.display_info()
			self.state_B()
		if self.tape[self.tape_position] == 1:
			self.tape[self.tape_position] = 1            
			self.move_left()
			self.state = "C"
			self.display_info()
			self.state_C()

	def state_B(self):
		if self.tape[self.tape_position] == 0:
			self.tape[self.tape_position] = 1
			self.move_left()
			self.state = "A"
			self.display_info()
			self.state_A()
		if self.tape[self.tape_position] == 1:
			self.tape[self.tape_position] = 1
			self.move_right()
			self.state = "B"
			self.display_info()
			self.state_B()

	def state_C(self):
		if self.tape[self.tape_position] == 0:
			self.tape[self.tape_position] = 1
			self.move_left()
			self.state = "B"
			self.display_info()
			self.state_B()
		if self.tape[self.tape_position] == 1:
			self.tape[self.tape_position] = 1
			self.end_count+=1
			self.state = "H"
			self.display_info()
			#print "end count: {}".format(self.end_count)
			sys.exit("HALT Condition reached!")
			#No move
			#Halt           
if __name__ == "__main__":	
	bb = Busy_Beaver()
	bb.state_A()

