eps=0.5;
pre_eps=eps;
while (1+eps)!=1:
	pre_eps=eps;
	eps=eps/2;
print("MACHINE EPSILON IN PYTHON IS ",pre_eps);

