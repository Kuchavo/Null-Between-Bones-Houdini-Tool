# === Null Between Bones Tool ===
# Contributors: Igor Kuchavo
# Requires at least: Houdini 15
# Tested up to: Houdini FX 16.5
# Version: 1.0.0

sel = hou.sortedNodes(hou.selectedNodes())

# cicle for all selected bones
for x, bone in enumerate(sel):

    outNode = hou.node('obj/chain_bone' + str(sel[x-1].path()[-1]) + '/')
    
    if x != int(len(sel)-1) and x != 0:
        # create and input Null nodes
        ctrl = hou.node('/obj').createNode('null', 'Control1')
        ctrl.insertInput(0, outNode)
        sel[x].insertInput(0, ctrl)
        # lenght correction
        strrr = '-ch("../chain_bone' + str(sel[x-1].path()[-1]) + '/length")'
        corNull = ctrl.setParmExpressions({"tz": strrr})
        # change controllers
        chi = ctrl.children()[0]
        chi.setParms({'displayicon': 1, 'scale': 2})
        # align node position
        ctrl.moveToGoodPosition()
        
    elif x == int(len(sel)-1):
        # create and input Null node on the last bone
        ctrl = hou.node('/obj').createNode('null', 'Control1')
        ctrl.insertInput(0, outNode)
        sel[-1].insertInput(0, ctrl)
        # lenght correction
        strrr = '-ch("../chain_bone' + str(sel[x-1].path()[-1]) + '/length")'
        corNull = ctrl.setParmExpressions({"tz": strrr})
        # change controllers
        chi = ctrl.children()[0]
        chi.setParms({'displayicon': 1, 'scale': 2})
        # align node position
        sel[x].moveToGoodPosition()
        ctrl.moveToGoodPosition()
