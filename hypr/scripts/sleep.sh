#!/bin/sh
swayidle -w \
                timeout 1200 'temp=$(brightnessctl g); brightnessctl set $((temp / 2))' \
                    resume 'temp=$(brightnessctl g); brightnessctl set $((temp * 2))' \
                timeout 1300 'swaylock -f & sleep 1' \
                timeout 1500 'hyprctl dispatch dpms off' \
                    resume 'hyprctl dispatch dpms on' \
                timeout 2000 'systemctl suspend'
