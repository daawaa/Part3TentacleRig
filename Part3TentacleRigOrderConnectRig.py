#parent CTRLs in hierarchical order 
skinBoneArray = cmds.ls(sl=1, o=1) 
CTRLArray     = cmds.ls(sl=1, o=1) 
for i in range (0, len(CTRLArray),1):
    parentObj = -1-i
    childObj = -2-i
    if parentObj !=0:
        pm.parent (CTRLArray[parentObj], CTRLArray[childObj])

#Connect bones to CTRLS
for i in range (0,len(jointArray)-1,1):
    pm.parentConstraint (CTRLArray[i],jointArray[i], mo=True)
       
