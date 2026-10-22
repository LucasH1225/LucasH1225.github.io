---
title: Learning and Planning for Robot Coverage
description: An ongoing study of hybrid Q-learning and structured planning for coverage and boundary service in grid simulation.
permalink: /projects/robot-coverage/
lead: Combining learned decisions with structured planning to cover cluttered spaces—and understanding what each part contributes.
summary: Exploring how Q-learning and structured planning routines can work together to cover cluttered spaces, through reproducible simulation experiments.
status: Research in progress
context_label: Setting
context: Grid simulation
stack: Python, PyTorch, Webots
featured: true
featured_order: 2
image: /assets/personal/robot-coverage.webp
image_alt: Two grid simulations comparing A-star planning and a hybrid learned coverage controller
image_width: 900
image_height: 506
image_caption: An illustrative paired simulation. One trajectory is not evidence of general superiority.
thumbnail_class: research-thumbnail
---

## Visiting the whole space

A robot can make sensible local moves and still leave small pockets of a room untouched. Covering an entire work area asks a different question from finding a route to one destination: how should the robot keep moving while recovering the regions it has missed?

This research explores that question through a hybrid controller. A compact Q network scores actions, while structured planning routines handle routing, turns, stagnation and remaining uncovered regions. The current task also requires service around certain obstacle boundaries, so finishing the floor alone does not count as completing the full task.

## Learning chooses within a structure

The learned component does not directly issue wheel commands. It selects among constrained movement and higher-level routines, including seeking uncovered cells and approaching or tracing obstacle boundaries. Action masks and persistent routine state determine which choices are feasible.

This makes the division of responsibility central to the project. A successful trajectory may owe as much to deterministic recovery as to a Q value. The evaluation therefore compares the complete system with a fixed-rule scheduler using the same routines, an A* comparator, and a version with a residual-region guard disabled.

<figure class="inline-figure">
  <a href="/assets/personal/robot-decision-stack.webp"><img src="/assets/personal/robot-decision-stack.webp" alt="Decision-stack diagram separating observed map and pose information from simulator-derived obstacle-service information entering the hybrid controller" width="1500" height="775" loading="lazy"></a>
  <figcaption>The decision stack from the working manuscript. Simulator-derived task information is a disclosed input, not a sensor measurement. <a href="/assets/personal/robot-decision-stack.webp">View the diagram</a></figcaption>
</figure>

## What the experiments currently show

The working manuscript separates historical development from a prospective holdout of 900 paired, 32 × 32 grid episodes across nine scenario families. Under the specified joint coverage-and-service protocol:

| Controller | Completed tasks |
| --- | ---: |
| Selected hybrid configuration | 900 / 900 |
| Nearest-uncovered/frontier A* comparator | 874 / 900 |
| Fixed-rule scheduler with shared routines | 882 / 900 |

Completion and efficiency tell different stories. On the episodes completed by both systems, A* was faster in simulated motion time than the selected hybrid configuration. The hybrid was faster than the rule scheduler on their mutually completed episodes. The residual-region guard also reduced motion time in its matched comparison, although both guard settings completed all 900 tasks.

These are results for one selected training lineage and a fixed simulator distribution. They support examining the scheduler and recovery rules under this protocol; they do not establish superiority over all classical planners or robustness across independently trained policies.

## The information boundary matters

The evaluated controller is **oracle-assisted**: some obstacle-service labels, component identities and progress-dependent rules use simulator truth. Restricting hidden collision information during policy previews does not make the whole decision stack sensor-only. Pose and heading are also assumed exact.

Making those assumptions explicit has become part of the research itself. Reproducible comparisons require recording what each controller knows, using matched maps and motion costs, and distinguishing floor coverage from the additional service endpoint.

## Where it is now

The manuscript is in preparation. Current work centres on checking the evidence, documenting the information contract and keeping the results separate from broader claims. This is a simulation study; the complete system has not been validated as a sensor-only controller on a real robot.
