import wmoc

# open an example network and creat a transient model
inp_file = 'examples/networks/Tnet1.inp'
tm = wmoc.network.TransientModel(inp_file)

# set wavespeed
tm.set_wavespeed(1200.)

#set time step
dt = 0.05  # time step [s], if not given, use the maximum allowed dt
tf = 20 # simulation peroid [s]
tm.set_time(tf)


# set valve closing 
tc = 2 # valve closure peroid [s]
ts = 0 # valve closure start time [s]
se = 0 # end open percentage [s]
m = 1 # closure constant [dimensionless]
valve_op = [tc,ts,se,m]
tm.valve_closure('9',valve_op)

# Initialize
t0 = 0. # initialize the simulation at 0 [s]
engine = 'WNTR' # or Epanet
tm = wmoc.simulation.Initializer(tm, t0, engine)

# Transient simulation
tm = wmoc.simulation.MOCSimulator(tm)

# report results 
import matplotlib.pyplot as plt

node = '2'
node = tm.get_node(node)
fig = plt.figure(figsize=(10,4), dpi=80, facecolor='w', edgecolor='k')
plt.plot(tm.simulation_timestamps,node.head)
plt.xlim([tm.simulation_timestamps[0],tm.simulation_timestamps[-1]])
plt.title('Pressure Head at Node %s '%node)
plt.xlabel("Time")
plt.ylabel("Pressure Head (m)")
plt.legend(loc='best')
plt.grid(True)
plt.show()