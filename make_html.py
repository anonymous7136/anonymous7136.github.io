from glob import glob 
import os 
f = glob ("./samples/*")


html = """
"""

model_name = ["gt", "hifigan", "istftnet", "bigvgan", "vocos", "compxgan"]



for i in f: 
    basename = os.path.basename(i)
    print(basename)
    html += f"""
<div>
<h3 id="">{basename}</h3>    
<table>
<thead>
<tr>
    <th>Ground-Truth</th>
    <th>HiFiGAN (V1)</th>
    <th>iSTFTNet</th>
    <th>BigVGAN (base)</th>
    <th>Vocos</th>
    <th>CompXGAN</th>
</tr>
</thead>
"""

    g = glob(f"./samples/{basename}/gt/*")
    for j in g:
        sample_name= os.path.basename(j)
        html +="<tbody>\n"
        html +="<tr>\n"
        for k in model_name:
            path = f"samples/{basename}/{k}/{sample_name}"
            html += f"<td><audio controls style=\"width: 225px; height: 50px\"><source src=\"{path}\" type=\"audio/wav\"></audio></td>\n"
        html +="</tr>\n"
        html +="</tbody>\n"
    html +="</table>\n"
    html+="</div>"

f = open("./samples.html", "w")
f.write(html)