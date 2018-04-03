# Examples taken from https://www.youtube.com/watch?v=oxf3o8IbCk4
import tensorflow as tf

#create two placeholders (for two floats)
x  = tf.placeholder(tf.float32)
y  = tf.placeholder(tf.float32)

#create two nodes that do the following:
# add the values then multiple the value by 3
adder_node = x + y
add_and_triple = adder_node*3

#create a session to use our nodes
sess  = tf.Session()
#or create a remote session
#tf.Session("grpc://example.org:2222")

# pass thru sample values
print "sess.run(add_and_triple, {x:3, y:4.5}): ", sess.run(add_and_triple, {x:3, y:4.5})
print "sess.run(add_and_triple, {x:[3, 8], y:[4.5, 9.1]}): ", sess.run(add_and_triple, {x:[3, 8], y:[4.5, 9.1]})
sess.close()

# let's look at things with tensorgraph
tf.reset_default_graph()#reset graph

a = tf.constant(5, name="input_a")
b = tf.constant(3, name="input_b")
c = tf.multiply(a,b, name="multiply_c")
d = tf.add(a,b, name="add_d")
e = tf.add(c,d, name="add_e")

sess = tf.Session()
output = sess.run(e)
writer = tf.summary.FileWriter("./my_graph", sess.graph)
writer.close()
sess.close()
