import time, string

# Das Resultat ist: Millisekunden/Funktionsaufrauf

def timef(f, args=(), repeat=10000):
    print 'CPU Times:'
    reps=repeat/10
    if reps < 1: reps=1
    repeat=reps*10
    reps=range(reps)
    clock=time.clock
    n=get_null(f)
    a=apply
    r=args

    a(n,r); a(n,r); a(n,r)
    t1=clock()
    for i in reps:
        a(n,r); a(n,r); a(n,r); a(n,r); a(n,r); 
        a(n,r); a(n,r); a(n,r); a(n,r); a(n,r)
    t2=clock()
    a(f,r); a(f,r); a(f,r)
    t3=clock()
    for i in reps:
        a(f,r); a(f,r); a(f,r); a(f,r); a(f,r); 
        a(f,r); a(f,r); a(f,r); a(f,r); a(f,r)
    t4=clock()
    a(n,r); a(n,r); a(n,r)
    t5=clock()
    for i in reps:
        a(n,r); a(n,r); a(n,r); a(n,r); a(n,r); 
        a(n,r); a(n,r); a(n,r); a(n,r); a(n,r)
    t6=clock()
    print 'Repeat:', repeat
    print 'Begin:', t1, 'End:', t2, t2 - t1
    print 'Begin:', t3, 'End:', t4, t4 - t3
    print 'Begin:', t5, 'End:', t6, t6 - t5
    print "%s milliseconds/functioncall" % (1000*(t4-t3 - 0.5*(t2-t1+t6-t5))/repeat,)

def timef1(f, args=()):
    clock = time.clock
    print 'CPU Times:'
    t1=clock()
    apply(f, args)
    t2=clock()
    print 'Begin:', t1, 'End:', t2, t2 - t1
    print "%s milliseconds/functioncall" % (1000*(t2-t1))

def timer1(f, args=()):
    clock = time.time
    print 'Real Times:'
    t1=clock()
    apply(f, args)
    t2=clock()
    print 'Begin:', t1, 'End:', t2, t2 - t1
    print "%s milliseconds/functioncall" % (1000*(t2-t1))

def timer_real_once(f, args=(), kw = {} ):
  """Returns real time in milliseconds."""
  clock = time.time
  t1=clock()
  res = apply(f, args, kw)
  t2=clock()
  return res, (1000*(t2-t1))

# richtige Zeit seit Epoch verwenden

def timer(f, args=(), repeat=10000):
    print 'Real Times:'
    reps=repeat/10
    if reps < 1: reps=1
    repeat=reps*10
    reps=range(reps)
    clock=time.time
    n=get_null(f)
    a=apply
    r=args

    a(n,r); a(n,r); a(n,r)
    t1=clock()
    for i in reps:
        a(n,r); a(n,r); a(n,r); a(n,r); a(n,r); 
        a(n,r); a(n,r); a(n,r); a(n,r); a(n,r)
    t2=clock()
    a(f,r); a(f,r); a(f,r)
    t3=clock()
    for i in reps:
        a(f,r); a(f,r); a(f,r); a(f,r); a(f,r); 
        a(f,r); a(f,r); a(f,r); a(f,r); a(f,r)
    t4=clock()
    a(n,r); a(n,r); a(n,r)
    t5=clock()
    for i in reps:
        a(n,r); a(n,r); a(n,r); a(n,r); a(n,r); 
        a(n,r); a(n,r); a(n,r); a(n,r); a(n,r)
    t6=clock()
    print 'Repeat:', repeat
    print 'Begin:', t1, 'End:', t2, t2 - t1
    print 'Begin:', t3, 'End:', t4, t4 - t3
    print 'Begin:', t5, 'End:', t6, t6 - t5
    print "%s milliseconds/functioncall" % (1000*(t4-t3 - 0.5*(t2-t1+t6-t5))/repeat,)

def get_null(f):
    args=[]
    nd=f.func_defaults
    nd=nd and len(nd) or 0
    argcount=f.func_code.co_argcount
    for i in range(argcount-nd): args.append("a%d" % i)
    for i in range(argcount-nd, argcount): args.append("a%d=None" % i)
    flags=f.func_code.co_flags
    if flags & 4: args.append('*args')
    if flags & 8: args.append('**kw')
    s="def dummy(%s): pass\n" % string.join(args,',')
    d={}
    exec s in d
    return d['dummy']


def timeb(*args):
  apply(timef, args)
  apply(timer, args)
