from jinja2 import Template

complex = { 'step_1' : { 'h1' : ['s1h1A', 's1h1B', ''], 'h2' : [''], 'h3' : ['s1h3A'] },
         'step_2' : { 'h1' : [''], 'h2' : ['', ''], 'h3' : ['', 's2h3B', 's2h3C'] } }

simple = { 'step_1' : { 'h1' : 's1h1', 'h2' : 's1h2', 'h3' : 's1h3' },
           'step_2' : { 'h1' : 's2h1', 'h2' : 's2h2', 'h3' : 's2h3' } }
#         'step_2' : { 'h2' : 's2h2', 'h3' : 's2h3' } }

simple_loop = [
               { 'step_1' : 's1h1', 'step_2' : 's2h1' },
               { 'step_1' : 's1h2', 'step_2' : 's2h2' },
               { 'step_1' : 's1h3', 'step_2' : 's2h3' }
              ]

complex_loop = [
               { 'step_1' : 's1h1', 'step_2' : 's2h1' },
               { 'step_1' : 's1h2', 'step_2' : 's2h2' },
               { 'step_1' : 's1h3', 'step_2' : 's2h3' }
              ]

distinct_steps = []
all_hosts = []
for step in simple:
    distinct_steps.append(step)
    for host in simple[step]:
        all_hosts.append(host)

distinct_hosts = list(set(all_hosts))
print distinct_steps
print distinct_hosts

print 'loop.....'
for i in complex_loop:
    print i
print '................'
print 'Original : ', simple
data = []
for host in distinct_hosts:
    val = {}
    for step in distinct_steps:
        if host in simple[step]:
            r = simple[step][host]
            val[step] = simple[step][host]
    if len(val) == len(distinct_steps):
        data.append(val)
for item in data:
    print item


'''
print '============='
data = { 'step_1' : simple['step_1']['h1'], 'step_2' : simple['step_2']['h2'] }
#print data

#template_str = '{{step_1}} == True and {{step_2}} == False'
template_str = '"{{step_1}}" == "{{step_3}}"'
template = Template(template_str)

for data in simple_loop:
    print 'data     : ', data
    print 'template : ', template_str
    print 'rendered  : ', template.render(data)
    print 'eval     : ', eval(template.render(data))
    print '================================'
'''
new_data = { 'steps' : complex }
print new_data
#template_str = '{% for step in steps %}{{ step.h1 }}{% endfor %}'
hehe = { 'hehe' : complex['step_1']['h1'] }
print 'hehe : ', hehe
template_str = "{{ steps.step_1.h1|join('|')|urlencode }}"
template = Template(template_str)
print 'HAHA : ', template.render(new_data)



print '%%%%%%_________%%%%%%'


results = { 'results' : [ { 'key' : 's1h1' }, { 'key' : 's1h2' }, {'key' : 's1h1' } ] }
#{% if prev.update({'key' : result.key}) %}{% endif %}
:w

ts = "{% set prev = { 'key' : '' } %}{% for result in results %}{% if loop.index > 1 %}{% if result.key == prev.key %}True{% else %}False{ {loop.index}}{% endif %}{% endif %}{% if prev.update({'key' : result.key}) %}{% endif %}{% endfor %}"
print Template(ts).render(results)

data = { 'eval_steps' : {'step_1': {'criterion': u'atleast_one_host', 'condition': u'"{% if result.matched_line != None %}True{% endif %}"'}, 'step_2': {'criterion': u'atleast_one_host', 'condition': u'"{% if result.MS_HEAPSIZE|int < 12000 %}True{% endif %}"'}}}

print data

"""
  {% if loop.index == 1 %}
    {{' '*6}}- {{ step }}
  {% else %}
    {{1}}
  {% endif %}
"""
#temp = """{% for step in eval_steps %} inside {{ endfor }}"""
temp = """{% for result in results %} inside {% endfor %}"""
print temp

template = Template(temp)
print template.render(data)

