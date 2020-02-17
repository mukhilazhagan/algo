#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def iou(box1, box2):
    
    # box1 ->[ [x1, y1], [x2, y2] ]
    # box2 ->[ [x1, y1], [x2, y2] ]
    
    end1 = []
    end2 = []
    
    end1 = [ max(box1[0][0], box2[0][0] ) , max(box1[0][1], box2[0][1] ]
    end2 = [ min(box1[1][0], box2[1][0] ) , min(box1[1][1], box2[1][1] ]
    
    if end2[0] < end1[0] or end2[1]<end1[1]:
        print("There is no overlap")
    else:
        return [end1, end2]
    
    # Union = sum box1 + box2 - int 
