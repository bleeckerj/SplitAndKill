import c4d

def main():
	p = doc.GetActiveObject()
	c4d.CallCommand(14046, 0) # Split
	doc.SetActiveObject(p)
	c4d.CallCommand(12109, 0) # Delete
    
if __name__=='__main__':
    main()