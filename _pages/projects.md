---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

**Note: This site is currently under construction. Some sections may be incomplete.**

Coming Soon.

<!-- Causal Blocks World -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Causal Reasoning & Counterfactual Explanations for Robot Manipulation</summary>
  <div id="causal-blocks-world" markdown="1">
  I am leading a 8-person collaborative research project investigating the use of probabilistic causal generative models and Bayesian causal inference, for prediction, action-selection, and counterfactual explanations for mobile robots undertaking manipulation tasks in home-care and domestic assistance applications, to increase robustness of robot task execution and increase AI/robot trust and explainability with human end-users.  
  
  We have developed a causal world model encoding robot-world-task relationships using the PyBullet physics-based simulator, the robot decision-making process, and noise and uncertainties in robot sensing and manipulation actions. We developed Bayesian prediction and probabilistic optimal action-selection methods for the robot block stacking task as an exemplar application. We have integrated the reasoning methods into a ROS-based autonomy framework targeting the Toyota Human Support Robot hardware, including an Aruco marker based 3D perception system and ROS MoveIt motion-planner and manipulation system. [IROS Causality for Robotics Workshop paper](https://arxiv.org/abs/2308.06203).  
  
  We have demonstrated block tower stability prediction and next-best action selection for autonomous robot block tower construction using robot hardware, and in the Gazebo physics-based robot simulator.  
  
  We are now extending the project to formulate the robot-world-task model as a SCM and develop post-hoc counterfactual explanation methods to explain robot behaviour and tasks outcomes in terms of robot perceptions, decisions, and actions. These methods will be used to create a human-robot natural language explanation system for human support robots, and will be integrated with the [Ethical Black Box](https://www.robotips.co.uk/ethical-black-box) data recording system and [human-robot dialogue system](https://sites.google.com/view/icra22ws-cor-wotf/accepted-papers#h.14191a22e7c35daf_244) developed under the [RoboTIPS](https://www.robotips.co.uk/home) UK Research and Innovation EPSRC Established Career Fellowship awarded to Dr Marina Jarotka. Project Ref: [EP/S005099/1](https://gtr.ukri.org/projects?ref=EP%2FS005099%2F1).
  </div>
</details>

<!-- Assuring the Safety of UAVs for Mine Inspection (ASUMI) -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Assuring the Safety of UAVs for Mine Inspection (ASUMI)</summary>
  <div id="drones_in_mines" markdown="1"> 
  Made scientific, technical, and project management contributions to the [Assuring the Safety of UAVs for Mine Inspection (ASUMI) collaborative research project](https://www.york.ac.uk/assuring-autonomy/demonstrators/uav-boulby-mine/), as part of the [Assuring Autonomy International Programme](https://www.york.ac.uk/assuring-autonomy), a £12m initiative funded by Lloyd’s Register Foundation and the University of York.  

  * Proposed a novel framework for probabilistic causal discovery, causal Bayesian inference & post-hoc counterfactual explanations for autonomous drones in mine surveying tasks and published an IROS 2023 Causality for Robotics [workshop paper](https://arxiv.org/abs/2308.10047).
  * Leading the creation of a collaboration between the University of Oxford and the University of York to investigate the use of temporal logics and formal probabilistic model-checking methods to bridge high-level abstract functional, safety, social, legal, and ethical constraints of autonomous systems with symbolic probabilistic causal model representations of robot-world systems and causal Bayesian inference for prediction, planning, and counterfactual explanations — in aid of codifying the assurance of autonomous AI and robot systems.
  * Led a scientific trial to perform 3D scanning and mapping of a mine tunnel segment at the Boulby underground Lab in the [ICL Boulby Mine](https://www.icl-uk.uk/), using a bespoke LIDAR-camera-IMU SLAM software and hardware system from the ORI Dynamic Robot Systems group. Successfully generated a fully registered point cloud 3D SLAM map covering over 200m of tunnel length. Undertaking work to generate a colorized point cloud, colorized mesh representation, and a high-fidelity Gazebo simulation world to be used to test and validate autonomous drone behaviors in simulation.
  * Co-organized a 6-month extended hackathon. Organized project timeline, competition description, team planning documents, and presentations. Developed PX4 flight control unit and Robot Operating System (ROS) based aerial autonomy software, delivered an autonomy framework, and validated the framework in a physics-based Gazebo robot simulation mock-mine environment.
  </div>
</details>

<!-- CAR-DESPOT -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Causally-Informed POMDP Planning for Robots Under Confounded Decision-Making</summary>
  <div id="car-despot" markdown="1">
  I proposed and developed **CAR-DESPOT**, a novel structural causal model (SCM) based online POMDP robot planner that achieves better task-level planning and policy execution performance by addressing issues of confounding in the robot decision making process, using causal modelling and causal Bayesian inference to eliminate confounding errors. I also proposed a stochastic variational inference (SVI) based method to learn offline the parameterisation of the causal system transition model, used for planning, from ground truth model data. I developed both methods in the [Pyro probabilistic programming language](https://pyro.ai), built on PyTorch. I successfully validated the methods on a toy problem with an unobserved confounder: demonstrated the learned causal model is highly accurate, and the proposed planning method is more robust to confounding and produces overall higher performing policies than the baseline method.  
  
  IROS 2023 conference paper: [\[arXiv paper\]](https://arxiv.org/abs/2304.06848) [\[conference listing\]](https://events.infovaya.com/presentation?id=104849).  

  I also an invited talk on my research on causality for confounded POMDP planning problems for robotics at the \href{https://sites.google.com/view/iros23-causal-robots}{\emph{Causality for Robotics}} workshop at the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 2023 in Detroit, USA.  
  </div>
</details>

<!-- Team ORIon Team Lead (2021/22) -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Team ORIon Team Lead (2021/22)</summary>
  <div id="orion-team-lead" markdown="1">
  Led and grew Team ORIon, the ORI’s official student robotics competition and outreach team, as Team Lead (2021/22)
  
  * Performed the Team Lead role for Team ORIon during the 2021/22 academic year.
  * Led a team of 11 PhD, masters, and undergraduate students to develop complex autonomous behaviors to enable the Toyota Human Support Robot to assist people with everyday tasks around the 
  home, including fetching household objects, putting away the groceries, and acting as a robot party host.
  * Grew the team from 4 to 11 active members in 12 months and led a team refresh following a COVID-hiatus.
  * Led the coordination of the 11-person team participation in the [RoboCup@Home 2022 international robotics competition](https://athome.robocup.org/) Domestic Standard Platform League in   Bangkok, Thailand — one of the largest annual robotics competitions — with 14 different leagues and teams from across the world.
  * Raised £33k in total funding from the Oxford Engineering Science department, Oxford colleges, industry sponsors, and private donors to permit the competition attendance of all critical team personnel.
  * Awarded a £350 St Edmund Hall Postgraduate College Grant for participation at RoboCup@Home 2023.
  * Coordinated technical and software development of autonomous behaviors by the sub-teams.
  * Organized team recruitment activities, software and hardware training sessions, and social activities.
  * Coordinated public science outreach and robot demonstrations at University of Oxford events.
  * Continuing to support the team since August 2022 by consulting the leadership team on organizational and technical matters and advocating for departmental support.

  </div>
</details>

<!-- Team ORIon Task-Level Planning Sub-Team Lead (2021/22). -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Team ORIon Task-Level Planning Sub-Team Lead (2021/22).</summary>
  <div id="orion-task-level-planning" markdown="1">
  Coordinated the design and development of high-level autonomous robot behaviours to accomplish complex domestic tasks by drawing on capabilities provided by the other sub-teams (e.g., perception, manipulation, human-robot interaction) for the [RoboCup@Home](https://athome.robocup.org) 2022 competition and various team outreach activities.  
  
  Implemented complex behaviours as finite-state machines, using the ROS SMACH state machine package, robust to robot failure modes (eg manipulation failure) and sources of environmental uncertainty (eg object placement). Conducted verification and testing in Gazebo simulation and on robot hardware. Performed verification to ensure compliance of the autonomous behaviours developed for the RoboCup 2022 competition to rulebook task specifications.
  </div>
</details>



<!-- Decentralised MCTS for Robot Intelligence, Surveillance, and Reconnaissance Missions -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Decentralised MCTS for Robot Intelligence, Surveillance, and Reconnaissance Missions</summary>
  <div id="d-mcts" markdown="1">
  Simultaneous exploration and exploitation based on mutual information and present a general solution for scout–task coordination using decentralised Monte Carlo tree search (D-MCTS). We evaluate the performance of our algorithms in a multi-drone surveillance scenario.  
  
  Collaborated with UTS academic partners to increase task performance in heterogeneous multi-robot systems using dec-MCTS. Advised on UAS software and hardware design and field deployments; ran field trials (incl. role of safety pilot); and co-authored scientific papers.  
  
  Published a conference and workshop paper at ICRA 2021 on heterogeneous multi-robot teams for multi-drone surveillance applications. Won the [Best Paper Award](https://clearpathrobotics.com/blog/2021/06/clearpath-sponsors-swarm-robotics-workshop-showcases-new-robot-at-icra-2021) at the ICRA 2021 [Robot Swarms in the Real World Workshop](https://sites.google.com/view/realworldswarms).
  </div>
</details>

<!-- Scaleable Multi-Robot Exploration & Return in Apriori Unknown Environments -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Scaleable Multi-Robot Exploration & Return in Apriori Unknown Environments</summary>
  <div id="tas-dcrc-swarming" markdown="1">
  Developed C++/ROS based decentralised multi-agent robot control software and performed robot autonomy software and aircraft companion computer hardware integration, to deliver DST Group project outcomes for the [Trusted Autonomous Systems Defence-Led Cooperative Research Centre](https://tasdcrc.com.au). Led simulation- and hardware-in-the-loop (SITL, HITL) validation and lab-based autonomous flight validation activities.
  </div>
</details>

<!-- Autonomous Drone Navigation & Mapping in Mixed GNSS-Available Urban Environments -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Autonomous Drone Navigation & Mapping in Mixed GNSS-Available Urban Environments</summary>
  <div id="mixed-gnss-nav" markdown="1">
  Developed custom ArduCopter multi-rotor flight controller firmware and C++/ROS autonomy software to enable resilient drone navigation, localisation, and mapping in mixed GNSS-available urban environments, to deliver against DST Group commitments to the [Trusted Scalable Search with Expendable Drones project](https://tasdcrc.com.au/what-we-do/#trustedsearch) within the [Trusted Autonomous Systems Defence-Led Cooperative Research Centre](https://tasdcrc.com.au). Implemented adaptive use of SLAM and GNSS pose estimates (e.g., from GPS measurements) for hybrid localisation and stable automated localisation transitions. Performed validation through simulation and robot hardware indoor/outdoor flight trials.
  </div>
</details>

<!-- Project -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Project Name</summary>
  <div id="unique_id1" markdown="1">
  Project Description
  </div>
</details>

<!-- Project -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Project Name</summary>
  <div id="unique_id2" markdown="1">
  Project Description
  </div>
</details>

<!-- Project -->
<details>
  <summary style="font-weight: bold; cursor: pointer;">Project Name</summary>
  <div id="unique_id3" markdown="1">
  Project Description
  </div>
</details>


