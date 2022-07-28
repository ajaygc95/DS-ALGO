
# import collections

# input = [["Math", "Statistics"], ["Reading", "Writing"], ["Statistics", "Probability"], ["Writing", "Math"]]
# input = [["Trigonometry", "Reading"], ["Algebra", "Geometry"], ["Economics", "Trigonometry"], ["Geometry", "Economics"],  ["Reading", "Writing"]]
# def getMiddleCourse(courses):
    
#     hash_map = collections.defaultdict(str)
#     for course in courses:
#         hash_map[course[0]] = course[1]
      
#     main_course = set(hash_map.values())
    
#     start = None

#     for single_course in hash_map:
#         if single_course not in main_course:
#             start = single_course
#             break 
#     print(start)
#     res = [start]
    
#     while start in hash_map:
        
#         subject = hash_map[start]
#         res.append(subject)
#         start = subject
    
#     mid = len(res)//2
    
#     if len(res)%2 == 1:
#         return res[mid]
#     else:
#         return res[mid-1]

# to_print = getMiddleCourse(input)
# print(to_print)

from calendar import c
import typing

def random(planpoint_id, plan_name, plan_namespace):
    print(f"planpoint_id: {planpoint_id} ",)
    print(f"planpoint_id: {plan_name}",)
    print(f"planpoint_id: {plan_namespace}",)
    
def something(planpoint_id:str=None, plan_name= None, plan_namespace = None, **kwargs):

    print(f"planpoint_id: {planpoint_id}",)
    print(f"plan_name: {plan_name}",)
    print(f"plan_namespace: {plan_namespace}",)
    # if kwargs.get("extra"):
    #     print(f"extra: {kwargs.get('extra')}",)

def caller(**kwargs):
    something(**kwargs)

caller(planpoint_id="plan_point-id", plan_name= "plan_name", plan_namespace = "plan_namespace", extra="extara-param")

# something(planpoint_id="234123",plan_name="alksjd;fl", plan_namespace="apoisfjusa")