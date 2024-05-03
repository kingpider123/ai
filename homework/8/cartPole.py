import gymnasium as gym

env = gym.make("CartPole-v1", render_mode = "human")
observation, info = env.reset(seed = 42)
steps = 0

for _ in range(200):
    env.render()

    if observation[3] > 0:
        action = 1
    else:
        action = 0
    print("space: ",observation[0])
    print("vel: ",observation[1])  
    print("ang: ",observation[2])   
    print("angVel: ",observation[3])
    observation, reward, terminated, truncated, info = env.step(action)
    steps += 1
    print("step", steps)

    if terminated or truncated:
        observation, info = env.reset()
        steps = 0
        print()

env.close()