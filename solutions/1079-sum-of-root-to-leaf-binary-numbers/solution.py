class Solution(object):
    def sumRootToLeaf(self, root):
        if not root:
            return 0
            
        answer = []

        def root_analysis(node, current_string):
            if not node:
                return
            
            current_string += str(node.val)
            
            if not node.left and not node.right:
                answer.append(current_string)
                return
            
            root_analysis(node.left, current_string)
            root_analysis(node.right, current_string)

        root_analysis(root, "")
        
        result = 0
        for i in answer:
            result += int(i, 2)

        return result
