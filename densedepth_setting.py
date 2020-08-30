#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


import argparse
import demo_runner_me_all_depth_net as dr
import numpy as np
import os
import subprocess

def shell_source(script):
    """Sometime you want to emulate the action of "source" in bash,
    settings some environment variables. Here is a way to do it."""
    import subprocess, os
    pipe = subprocess.Popen(". %s; env" % script, stdout=subprocess.PIPE, shell=True)
    output = pipe.communicate()[0]
    env = dict((line.split("=", 1) for line in output.splitlines()))
    os.environ.update(env)

parser = argparse.ArgumentParser()
parser.add_argument("--width", type=int, default=620)
parser.add_argument("--height", type=int, default=480)
parser.add_argument("--scene", type=str, default="rtown.glb")
parser.add_argument("--max_frames", type=int, default=400)
parser.add_argument("--total_frames",type=int,default=0)
parser.add_argument("--save_png", action="store_true")
parser.add_argument("--sensor_height", type=float, default=1.5)
parser.add_argument("--disable_color_sensor", action="store_true")
parser.add_argument("--semantic_sensor", action="store_true")
parser.add_argument("--depth_sensor", action="store_true")
parser.add_argument("--print_semantic_scene", action="store_true")
parser.add_argument("--print_semantic_mask_stats", action="store_true")
parser.add_argument("--compute_shortest_path", action="store_true")
parser.add_argument("--compute_action_shortest_path", action="store_true")
parser.add_argument("--seed", type=int, default=1)
parser.add_argument("--silent", action="store_true")

args = parser.parse_args()


def make_settings():
    settings = dr.default_sim_settings.copy()
    settings["max_frames"] = args.max_frames
    settings["total_frames"]=args.total_frames
    settings["width"] = args.width
    settings["height"] = args.height
    settings["scene"] = args.scene
    settings["save_png"] = args.save_png
    settings["sensor_height"] = args.sensor_height
    settings["color_sensor"] = not args.disable_color_sensor
    settings["semantic_sensor"] = args.semantic_sensor
    settings["depth_sensor"] = args.depth_sensor
    settings["print_semantic_scene"] = args.print_semantic_scene
    settings["print_semantic_mask_stats"] = args.print_semantic_mask_stats
    settings["compute_shortest_path"] = args.compute_shortest_path
    settings["compute_action_shortest_path"] = args.compute_action_shortest_path
    settings["seed"] = args.seed
    settings["silent"] = args.silent

    return settings


settings = make_settings()

demo_runner = dr.DemoRunner(settings, dr.DemoRunnerType.EXAMPLE)
frames=0

Vx=float(0)
Vy=float(0)
Vz=float(0)
Wx=float(0)
Wy=float(0)
Wz=float(0)

demo_runner.example(Vx,Vy,Vz,Wx,Wy,Wz,frames)

print(" ============ Performance ======================== ")
print(
    " %d x %d, total time: %0.3f sec."
)
print(" ================================================= ")
