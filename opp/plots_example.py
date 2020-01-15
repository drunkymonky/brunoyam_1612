from math import sin

import matplotlib.pyplot as plt

y = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00099945068359375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009996891021728516, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00099945068359375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009996891021728516, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009996891021728516, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0010001659393310547, 0.0, 0.0, 0.00099945068359375, 0.0, 0.0009999275207519531, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009996891021728516, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0010004043579101562, 0.0, 0.0, 0.0, 0.0009992122650146484, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00099945068359375, 0.0009999275207519531, 0.0, 0.0, 0.00099945068359375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009996891021728516, 0.0009999275207519531, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0010001659393310547, 0.0, 0.0, 0.0, 0.00099945068359375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009996891021728516, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0009980201721191406, 0.0009996891021728516, 0.0, 0.0, 0.0, 0.0010008811950683594, 0.0009996891021728516, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0009996891021728516, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0010001659393310547, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0009999275207519531, 0.0, 0.0009996891021728516, 0.0, 0.0, 0.0, 0.0, 0.00099945068359375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0009984970092773438, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0009992122650146484, 0.0, 0.00099945068359375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009996891021728516, 0.0, 0.0, 0.0, 0.0010013580322265625, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0010008811950683594, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009996891021728516, 0.0009999275207519531, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.00099945068359375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0, 0.0, 0.0009996891021728516, 0.0, 0.0, 0.0, 0.0]
x = [x for x in range(len(y))]
y_2 = [0.0, 0.0, 0.0, 0.0009982585906982422, 0.0, 0.0, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.00099945068359375, 0.0, 0.0009999275207519531, 0.00099945068359375, 0.0, 0.0009999275207519531, 0.0, 0.0, 0.0009992122650146484, 0.0, 0.0, 0.0009996891021728516, 0.0, 0.0029990673065185547, 0.0009996891021728516, 0.0, 0.00099945068359375, 0.0, 0.0010006427764892578, 0.0, 0.0, 0.0009989738464355469, 0.0, 0.00099945068359375, 0.0, 0.0009999275207519531, 0.0, 0.0, 0.0009999275207519531, 0.0, 0.0009992122650146484, 0.0, 0.0009999275207519531, 0.0, 0.0009999275207519531, 0.00099945068359375, 0.0, 0.0009996891021728516, 0.0, 0.0009996891021728516, 0.0, 0.0009996891021728516, 0.0, 0.0009996891021728516, 0.0, 0.0, 0.0009996891021728516, 0.0, 0.00099945068359375, 0.0, 0.0009996891021728516, 0.0009996891021728516, 0.0010004043579101562, 0.0010001659393310547, 0.0, 0.0009989738464355469, 0.0009989738464355469, 0.0, 0.0009996891021728516, 0.00099945068359375, 0.0010001659393310547, 0.00099945068359375, 0.0010001659393310547, 0.00099945068359375, 0.0, 0.0, 0.00099945068359375, 0.0010001659393310547, 0.0, 0.00099945068359375, 0.0009992122650146484, 0.0010006427764892578, 0.00099945068359375, 0.00099945068359375, 0.00099945068359375, 0.0, 0.0, 0.0010001659393310547, 0.0009989738464355469, 0.0010004043579101562, 0.0009992122650146484, 0.00099945068359375, 0.0009996891021728516, 0.0009992122650146484, 0.0010004043579101562, 0.0, 0.00099945068359375, 0.0009992122650146484, 0.0009999275207519531, 0.0009996891021728516, 0.0009996891021728516, 0.0009999275207519531, 0.00099945068359375, 0.00099945068359375, 0.0009999275207519531, 0.00099945068359375, 0.0009999275207519531, 0.001999378204345703, 0.0010008811950683594, 0.0009984970092773438, 0.0009992122650146484, 0.0009999275207519531, 0.0009996891021728516, 0.0009996891021728516, 0.0009996891021728516, 0.001999378204345703, 0.0010001659393310547, 0.0009989738464355469, 0.00099945068359375, 0.0010006427764892578, 0.0009992122650146484, 0.0019996166229248047, 0.0009992122650146484, 0.0009996891021728516, 0.0, 0.0, 0.0009996891021728516, 0.0009999275207519531, 0.0009999275207519531, 0.0009992122650146484, 0.0010001659393310547, 0.0009992122650146484, 0.0009996891021728516, 0.0009999275207519531, 0.0019996166229248047, 0.0010001659393310547, 0.0019981861114501953, 0.0009996891021728516, 0.0010006427764892578, 0.0009987354278564453, 0.0019996166229248047, 0.0009996891021728516, 0.0010001659393310547, 0.0009989738464355469, 0.0009999275207519531, 0.0009992122650146484, 0.0029993057250976562, 0.00099945068359375, 0.0010004043579101562, 0.0009989738464355469, 0.001999378204345703, 0.0019998550415039062, 0.0009992122650146484, 0.00099945068359375, 0.0009989738464355469, 0.0009999275207519531, 0.0019998550415039062, 0.00099945068359375, 0.0009996891021728516, 0.0019989013671875, 0.0009999275207519531, 0.0019996166229248047, 0.0019989013671875, 0.0019991397857666016, 0.0010001659393310547, 0.00099945068359375, 0.0009996891021728516, 0.0019991397857666016, 0.0019991397857666016, 0.0010001659393310547, 0.0010001659393310547, 0.0019991397857666016, 0.0010004043579101562, 0.0019986629486083984, 0.0009996891021728516, 0.0019991397857666016, 0.0019996166229248047, 0.0010001659393310547, 0.0029985904693603516, 0.00099945068359375, 0.001999378204345703, 0.0019998550415039062, 0.0019981861114501953, 0.0010006427764892578, 0.0029985904693603516, 0.0019991397857666016, 0.001999378204345703, 0.0019991397857666016, 0.002999544143676758, 0.0019986629486083984, 0.0019998550415039062, 0.001999378204345703, 0.0029990673065185547, 0.002999544143676758, 0.0029993057250976562, 0.0029985904693603516, 0.001998424530029297, 0.0019998550415039062, 0.0019986629486083984, 0.003999471664428711, 0.0019991397857666016, 0.0009999275207519531, 0.0009992122650146484, 0.003998517990112305, 0.001999378204345703, 0.002998828887939453, 0.0029985904693603516, 0.003999471664428711, 0.0019996166229248047, 0.001998424530029297, 0.0019998550415039062, 0.003999471664428711, 0.0019981861114501953, 0.0019989013671875, 0.0019991397857666016, 0.003999948501586914, 0.004997730255126953, 0.0019991397857666016, 0.0019989013671875, 0.0020003318786621094, 0.0029993057250976562, 0.003998756408691406, 0.003000497817993164, 0.001998424530029297, 0.002998828887939453, 0.0019989013671875, 0.003999948501586914, 0.00299835205078125, 0.0029997825622558594, 0.0029985904693603516, 0.0019996166229248047, 0.003999233245849609, 0.003999471664428711, 0.002997875213623047, 0.001998424530029297, 0.0029997825622558594, 0.003998517990112305, 0.0029985904693603516, 0.0029990673065185547, 0.0029993057250976562, 0.0029985904693603516, 0.003999233245849609, 0.0019979476928710938, 0.003998994827270508, 0.0029985904693603516, 0.003000020980834961, 0.0029981136322021484, 0.002999544143676758, 0.0039980411529541016, 0.0029993057250976562, 0.002998828887939453, 0.003998517990112305, 0.0029993057250976562, 0.003998517990112305, 0.0029997825622558594, 0.003998279571533203, 0.002998828887939453, 0.003998517990112305, 0.006998300552368164, 0.003998756408691406, 0.003998279571533203, 0.004000663757324219, 0.002996683120727539, 0.003998756408691406, 0.005998849868774414, 0.0039980411529541016, 0.003998756408691406, 0.006997823715209961, 0.0029990673065185547, 0.01299595832824707, 0.00899648666381836, 0.010996580123901367, 0.01399540901184082, 0.008997678756713867, 0.003998517990112305, 0.0029990673065185547, 0.003998279571533203, 0.003998756408691406, 0.003998994827270508, 0.0039980411529541016, 0.0039997100830078125, 0.003998279571533203, 0.0039980411529541016, 0.003998756408691406, 0.003998994827270508, 0.003998279571533203, 0.003998756408691406, 0.003998517990112305, 0.0029993057250976562, 0.0029985904693603516, 0.003999233245849609, 0.003998994827270508, 0.003998279571533203, 0.0039980411529541016, 0.004998683929443359, 0.004998683929443359, 0.003998279571533203, 0.004998922348022461, 0.005998134613037109, 0.003998279571533203, 0.003998756408691406, 0.0039980411529541016, 0.00499725341796875, 0.005999565124511719, 0.003998517990112305, 0.006996870040893555, 0.004998445510864258, 0.0069980621337890625, 0.0039980411529541016, 0.0069980621337890625, 0.005997896194458008, 0.005997657775878906, 0.003998994827270508, 0.007998466491699219, 0.00499725341796875, 0.003998756408691406, 0.0059986114501953125, 0.0049974918365478516, 0.003998756408691406, 0.004998445510864258, 0.0039980411529541016, 0.004998683929443359, 0.004998207092285156, 0.004998445510864258, 0.004999399185180664, 0.004996776580810547, 0.004998922348022461, 0.003998756408691406, 0.004998683929443359, 0.004998445510864258, 0.003997802734375, 0.004998207092285156, 0.004998207092285156, 0.0049991607666015625, 0.003998279571533203, 0.0039975643157958984, 0.003998994827270508, 0.0070018768310546875, 0.003996133804321289, 0.0049991607666015625, 0.004997730255126953, 0.005002021789550781, 0.004994869232177734, 0.0039975643157958984, 0.0049974918365478516, 0.004998445510864258, 0.005999088287353516, 0.00499725341796875, 0.004999637603759766, 0.006996631622314453, 0.0049991607666015625, 0.004997968673706055, 0.006000995635986328, 0.004995584487915039, 0.005997419357299805, 0.005998373031616211, 0.005998134613037109, 0.0049974918365478516, 0.005998134613037109, 0.004998683929443359, 0.005998134613037109, 0.004998445510864258, 0.005997419357299805, 0.004998683929443359, 0.004998207092285156, 0.004998445510864258, 0.005998134613037109, 0.004999399185180664, 0.005998134613037109, 0.005998134613037109, 0.0059964656829833984, 0.004998207092285156, 0.004998207092285156, 0.005998134613037109, 0.005998134613037109, 0.012995719909667969, 0.005999326705932617, 0.005997180938720703, 0.005998849868774414, 0.005997180938720703, 0.005998134613037109, 0.005997657775878906, 0.006997346878051758, 0.005998373031616211, 0.005997180938720703, 0.006997585296630859, 0.005998373031616211, 0.007000923156738281, 0.005994558334350586, 0.006999492645263672, 0.0069959163665771484, 0.005998849868774414, 0.005997419357299805, 0.005997657775878906, 0.005997896194458008, 0.0059986114501953125, 0.005998134613037109, 0.005997896194458008, 0.005997419357299805, 0.0059986114501953125, 0.006997108459472656, 0.005999326705932617, 0.0059986114501953125, 0.006997108459472656, 0.006997585296630859, 0.00699615478515625, 0.012996435165405273, 0.010996103286743164, 0.007998943328857422, 0.006997346878051758, 0.0069963932037353516, 0.006997108459472656, 0.006999492645263672, 0.006997108459472656, 0.0069963932037353516, 0.007999658584594727, 0.007997274398803711, 0.011995792388916016, 0.007997274398803711, 0.006997108459472656, 0.007997512817382812, 0.006997585296630859, 0.006997346878051758, 0.0069980621337890625, 0.006997585296630859, 0.007997274398803711, 0.006997346878051758, 0.007997512817382812, 0.006997585296630859, 0.007997512817382812, 0.006997585296630859, 0.0069997310638427734, 0.007995367050170898, 0.007997274398803711, 0.007999658584594727, 0.006995677947998047, 0.007997274398803711, 0.007998943328857422, 0.007995843887329102, 0.007997512817382812, 0.007998466491699219, 0.007996320724487305, 0.008997678756713867, 0.008996248245239258, 0.007998228073120117, 0.007996797561645508, 0.00799703598022461, 0.007997512817382812, 0.007997751235961914, 0.007996797561645508, 0.007998228073120117, 0.00799703598022461, 0.007996797561645508, 0.007995843887329102, 0.007997512817382812, 0.008996725082397461, 0.007999420166015625, 0.007996320724487305, 0.008996963500976562, 0.008997678756713867, 0.008000850677490234, 0.007994651794433594, 0.008996009826660156, 0.009996175765991211, 0.008998870849609375, 0.008995294570922852, 0.008997917175292969, 0.00899648666381836, 0.007997274398803711, 0.008996725082397461, 0.008997917175292969, 0.00899648666381836, 0.008996725082397461, 0.008998394012451172, 0.008997201919555664, 0.008996725082397461, 0.008997440338134766, 0.008995294570922852, 0.008998394012451172, 0.008997201919555664, 0.008997440338134766, 0.008996009826660156, 0.008998632431030273, 0.010996341705322266, 0.009996652603149414, 0.008996248245239258, 0.009999513626098633, 0.009995460510253906, 0.009994745254516602, 0.008998632431030273, 0.00899505615234375, 0.009996891021728516, 0.009996652603149414, 0.009998083114624023, 0.008996963500976562, 0.008995771408081055, 0.009996414184570312, 0.009996652603149414, 0.009996652603149414, 0.009996652603149414]
# plt.plot(x, y, x, y_2)
plt.plot(x, [sin(k) for k in x ])
plt.title("My plot")

plt.show()
