"""
The wmoc.network.control module includes method to define 
network controls of the pump and valve.These control modify 
parameters in the network during trasient simulation. 

"""
import numpy as np

def valvesetting(dt, tf, valve_op):
    """Define valve operation curve (percentage open v.s. time)
    
    Parameters
    ----------
    dt : float
        Time step
    tf : float 
        Simulation Time
    valve_op : list 
        Contains paramtes to defie valve operation rule
        valve_op = [tc,ts,se,m]
        tc : the duration takes to close the valve [s]
        ts : closure start time [s]
        se : final open percentage [s]
        m  : closure constant [unitless]

    Returns
    -------
    s : list 
        valve operation curve 
    """

    [tc,ts,se,m] = valve_op
    tn = int(tf/dt)
    # aburupt closure 
    if tc ==0:
        s =  np.array([(1- (i*dt- ts))**1    for i in range(tn)])
        s[s>1] = 1
        s[s<1] = se
    # gradual closure 
    else:
        s =  np.array([(1- (i*dt- ts)/tc)**m    for i in range(tn)])
        s[s>1] = 1
        s[s<se] = se
    return s   

def pumpsetting(dt, tf, pump_op):
    """Define pump operation curve (percentage open v.s. time)
    
    Parameters
    ----------
    dt : float
        Time step
    tf : float 
        Simulation Time
    valve_op : list 
        Contains paramtes to defie valve operation rule
        valve_op = [tc,ts,se,m]
        tc : the duration takes to close the valve [s]
        ts : closure start time [s]
        se : final open percentage [s]
        m  : closure constant [unitless]

    Returns
    -------
    s : list 
        valve operation curve 
    """
    [tc,ts,se,m] = pump_op
    tn = int(tf/dt)
    # gradual closure 
    if tc != 0:
        s =  np.array([(1- (i*dt- ts)/tc)**m    for i in range(tn)])
        s[s>1] = 1
        s[s<se] = se
    
    # aburupt closure 
    if tc ==0:
        s =  np.array([(1- (i*dt- ts))**1    for i in range(tn)])
        s[s>1] = 1
        s[s<1] = se  
        
    return s