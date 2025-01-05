#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class TektonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tekton"

    @property
    def original_file_name(self) -> "str":
        return "tekton.svg"

    @property
    def title(self) -> "str":
        return "Tekton"

    @property
    def primary_color(self) -> "str":
        return "#FD495C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tekton</title>
     <path d="M1.8823.0002a.924.924 0 0 0-.8906.6777A6.4647 6.4647 0 0
 0 .8042 3.133a6.6196 6.6196 0 0 0 .7578 2.3672 7.283 7.283 0 0 0
 .9062 1.3066 9.7647 9.7647 0 0 0-.125.7852 10.1225 10.1225 0 0
 0-.0722 1.3594c.003.1862.008.375.0293.5644.0428.5405.5351 1.1816.871
 1.5938a7.1354 7.1354 0 0 0 2.0255 1.7168.9098.9098 0 0 0
 .0332.082c.0827.1763.1864.342.3105.4922a5.9281 5.9281 0 0 0-.5058
 1.6738 8.1648 8.1648 0 0 0-.1739 1.3008 2.218 2.218 0 0 0-.4629.2832
 2.6568 2.6568 0 0 0-.8457 1.2305 3.252 3.252 0 0
 0-.1093.4101l-.2286-.0625-.0253.1602c-.116.7298-.0639 1.3615.2324
 2.0058a1.4432 1.4432 0 0 0-.6934.293 1.2313 1.2313 0 0
 0-.3535.459c-.1466.3298-.293.7136-.293 1.08 0
 .2719.085.5437.2989.7208a.7112.7112 0 0 0
 .4492.162h2.3691c.1405.3726.4097.7205.8067.8243.112.0274.2264.0439.3418.0469.122.006.2402.0078.3593.0078.3085.0061.6174.003.9258
 0 .4825-.0061.9657-.0151 1.4512-.0274a.7688.7688 0 0 0
 .6777-.4433.7727.7727 0 0 0 .6817.4433c.4824.0122.9647.0213
 1.4472.0274.3085 0 .6174.003.9258 0a7.143 7.143 0 0 0 .3594-.0078
 1.856 1.856 0 0 0
 .3398-.047c.397-.1038.6673-.4485.8047-.8241h2.3926a.7059.7059 0 0 0
 .4473-.1621c.2137-.1771.3007-.449.3007-.7207-.003-.3665-.1472-.7503-.2968-1.0801-.2107-.4673-.6103-.6878-1.0684-.752.2962-.6443.3485-1.276.2324-2.0058l-.0254-.1602-.205.0567c-.002-.008-.0053-.0194-.006-.0293a.3897.3897
 0 0 0 .0255-.0508 6.936 6.936 0 0 1 .4512-.8887 8.6153 8.6153 0 0 1
 .7421-1.0742 5.5548 5.5548 0 0 1 .459-.5078c.2901-.281.6561-.5155
 1.0684-.543.289-.0199.576.0648.8066.2402.1741.1314.2594.2812.3418.4766.1374.3329.2224.6174.4942.877.4824.455
 1.1993.464 1.7734.1953.449-.2107.8282-.5963.9473-1.088a1.326 1.326 0
 0 0
 .0312-.451c-.0946-.9193-.6603-1.7528-1.3535-2.336-.6321-.5314-1.4495-.92-2.2832-.9414-.7848-.0214-1.5592.221-2.2402.5996-1.1604.6443-2.0822
 1.6912-2.7754 2.8515a7.8763 7.8763 0 0 0-.0938-.5254 6.231 6.231 0 0
 0-.2363-1.0039 4.7875 4.7875 0 0 0-.17-.455 1.898 1.898 0 0 0
 .25-.3282 4.2022 4.2022 0 0 0 .2169-.3984l.037-.084a7.1704 7.1704 0 0
 0
 2.0235-1.7148c.3451-.4214.8223-1.0458.8711-1.6016.0214-.1863.0282-.3779.0313-.5703a9.9704
 9.9704 0 0 0-.0762-1.3828 11.9494 11.9494 0 0 0-.123-.748 7.288 7.288
 0 0 0 .9042-1.3087 6.6098 6.6098 0 0 0 .7579-2.3652 6.5344 6.5344 0 0
 0-.1836-2.455.9163.9163 0 0 0-.8887-.6817c-1.5636 0-2.914.6384-4.166
 1.4629a7.3538 7.3538 0 0 0-7.6836 0C4.7952.6386 3.4458 0 1.8823
 0zm.0176.92h.0742c.8673.4763 1.6438 1.4442 2.2149 2.4062a10.47 10.47
 0 0 0-.3399.4629 8.0257 8.0257 0 0 0-.9746
 2.0468c-.6993-.9405-1.5874-2.6692-.998-4.8984.0091-.003.0142-.0115.0234-.0176zm15.9082
 0h.0723l.0214.0214c.5894 2.2293-.2987 3.956-.998 4.8965a7.9805 7.9805
 0 0 0-1.0371-2.1406 5.536 5.536 0 0 0-.2735-.3711c.5711-.962
 1.3476-1.9299 2.2149-2.4063zM3.187 1.0997c.7726.2077 1.4993.5828
 2.1895 1.0195a7.1749 7.1749 0 0
 0-.791.7383c-.1314-.2168-.2743-.4271-.4239-.6348a7.4915 7.4915 0 0
 0-.9746-1.123zm13.4082 0a7.4917 7.4917 0 0 0-.9746
 1.123c-.1496.2077-.2895.4219-.4238.6387a7.2142 7.2142 0 0
 0-.791-.7422c.687-.4367 1.4168-.8119
 2.1894-1.0195zm-6.8867.17v2.5937c-1.3864.0305-2.7484.4153-3.582
 1.1543-.965.852-1.6093 2.3259-1.5391 3.1015.061.6932 1.1732 1.1678
 2.6543 1.4121a1.3476 1.3476 0 0 0-.1524.4278 1.9363 1.9363 0 0 0
 .002.6367 16.41 16.41 0 0 1-1.5137-.2442 14.9847 14.9847 0 0
 1-2.3242-.6953.9417.9417 0 0 1-.0605-.2207S2.8803 6.585 4.4682
 4.2092c1.2704-1.8995 3.2461-2.8814 5.2403-2.9395zm.3652 0c1.9605.0549
 3.904 1.006 5.1836 2.8534 1.6551 2.3911 1.336 5.3106 1.336
 5.3106a.8319.8319 0 0
 1-.0528.2129c-.758.298-1.5392.5337-2.336.7031-.4489.0947-.9528.18-1.5116.2441a1.9483
 1.9483 0 0 0 .0039-.6386 1.3514 1.3514 0 0 0-.1543-.4278c1.481-.2443
 2.5932-.7139
 2.6543-1.4101.0702-.7757-.5741-2.2515-1.5391-3.1035-.8367-.736-2.1976-1.1199-3.584-1.1504zm-.8535.7128a.2137.2137
 0 0 0-.2168.2168c0
 .1932.2345.289.3711.1524.1366-.1366.0389-.3692-.1543-.3692zm1.3418
 0a.2176.2176 0 0 0-.2168.2168c0
 .1932.2326.289.3691.1524.1366-.1366.0409-.3692-.1523-.3692zm-1.3418.955a.2176.2176
 0 0 0-.2168.2169c0
 .1932.2345.2909.3711.1543s.0389-.3711-.1543-.3711zm1.3418
 0a.2176.2176 0 0 0-.2168.2169c0
 .1932.2326.2909.3691.1543.1366-.1366.0409-.3711-.1523-.3711zm-3.5117
 3.756c.3303.0024.6414.151.8535.4042.2221.2618.3451.5943.3437.9375a.2196.2196
 0 0 1-.2207.2188.2196.2196 0 0 1-.2207-.2188.9864.9864 0 0
 0-.2304-.6484.7096.7096 0 0 0-.5293-.2539.6638.6638 0 0
 0-.379.1191.8426.8426 0 0 0-.287.3457.2166.2166 0 0
 1-.2891.1036c-.1088-.0515-.157-.1803-.1055-.2891a1.3353 1.3353 0 0 1
 .4375-.5234 1.1044 1.1044 0 0 1 .627-.1954zm5.6855 0c.2237 0
 .441.068.625.1953.1884.1332.3397.3144.4375.5234a.2183.2183 0 0
 1-.1054.289.2198.2198 0 0 1-.291-.1035.8427.8427 0 0
 0-.2872-.3457.6638.6638 0 0 0-.3789-.1191.7046.7046 0 0
 0-.5293.254.9864.9864 0 0 0-.2304.6483.2196.2196 0 0
 1-.2207.2149.2196.2196 0 0 1-.2207-.2149 1.427 1.427 0 0 1
 .3457-.9375 1.1282 1.1282 0 0 1 .8554-.4043zM9.8862
 8.8927h.0098c.9741-.0092 2.1613.4358 2.2773 1.1504.113.684-.2644
 1.1483-.8476
 1.414-.8643.3207-1.1684-.0976-1.3028-.3633-.064-.1282-.0914-.1942-.125-.1972h-.0078c-.0274.0122-.0626.0723-.1328.1914-.1374.2412-.421.6026-1.0195.4804-.736-.2382-1.2642-.7344-1.1328-1.5253.119-.7146
 1.307-1.1596 2.2812-1.1504zm.004.332c-.591
 0-1.3048.1726-1.375.539-.1161.6078.7855.9005 1.3808.899.5952-.0016
 1.487-.2943
 1.371-.899-.0702-.3664-.786-.539-1.3769-.539zm-6.3829.9102a14.973
 14.973 0 0 0 1.9961.5722 16.386 16.386 0 0 0 1.707.2676.8424.8424 0 0
 0 .084.1523c.2688.4612.7292.7517
 1.2422.9258-.2718.113-.4824.2914-.5312.5723a.6502.6502 0 0 0
 .0332.332c0 .003.0039.0087.0039.0117a9.4685 9.4685 0 0
 1-1.1817-.3164c-1.2123-.4183-2.2242-1.087-3.0273-2.0703a5.1977 5.1977
 0 0
 1-.3262-.4472zm12.7637.0039c-.0794.1068-.1614.2176-.25.3183-.455.5466-.9397
 1.0516-1.5352 1.4395-.8245.5374-1.7539.8718-2.7402 1.0703a.6467.6467
 0 0 0
 .0332-.3574c-.0519-.2718-.2558-.4457-.5215-.5586.513-.1741.9715-.4678
 1.2402-.9258a2.3064 2.3064 0 0 0 .0762-.1504 16.5172 16.5172 0 0 0
 1.707-.2676 15.187 15.187 0 0 0 1.9903-.5683zm-6.3477
 2.2265c.7513.002 1.4906.1452
 1.338.4414-.0703.1374-.2546.2412-.4806.3145-.293.0366-.5913.0617-.8906.08a17.0875
 17.0875 0 0
 1-.8867-.08c-.2413-.0794-.4322-.1941-.4902-.3438-.1039-.2733.6589-.414
 1.4101-.412zm9.6524.5098c.4672.0122.9528.1766
 1.3925.4453-.455.1313-.8269.5012-1.0253.9531a1.8268 1.8268 0 0
 0-.1309.4453 1.8991 1.8991 0 0 0-.7852-.2226.2515.2515 0 0
 0-.037-.0762c-.2657-.3603-.3026-1.0327.0058-1.3809a.7229.7229 0 0 1
 .0703-.0664 1.64 1.64 0 0 1 .1035-.08 2.6015 2.6015 0 0 1
 .4063-.0176zm-1.1211.17a1.6561 1.6561 0 0
 0-.1328.707c.0042.2725.071.5397.1972.7812a2.2462 2.2462 0 0
 0-.6894.2754.1692.1692 0 0
 0-.0547-.0352c-.171-.0732-.3174-.2405-.4121-.4023-.1038-.1802-.229-.5225-.0977-.7149
 0-.003.002-.0028.002-.0058.1435-.0977.2881-.1902.4316-.2696a4.4099
 4.4099 0 0 1
 .7559-.3359zm-11.9942.203c.1863.0672.3721.1306.5645.1856a6.0804
 6.0804 0 0 0 3.246.7168 5.9745 5.9745 0 0 0 1.4415-.2715 5.7607
 5.7607 0 0 0 1.0547-.4453 9.3597 9.3597 0 0 0 .5644-.1856 3.743 3.743
 0 0 1-1.9824 1.3711c.7176-.0916 1.4625-.276 2.0488-.621.3268.794.5109
 1.8688.3399
 3.2949-.0427.342-.096.6661-.1602.9746-.7329-.4093-1.7452-.0824-2.5117.3574-.0977-1.414-.403-2.455-.5312-2.8399-.1161-.3542-.5358-.2835-.545.0372.058.1557.0953.3596.129.5214.055.284.0998.5743.1425.8614.0702.4794.1442.9862.1777
 1.4687.0062.1069.0126.2174.0157.3242a5.5158 5.5158 0 0
 1-1.3828.0078c.003-.1099.0075-.2181.0136-.328.0153-.1955.04-.3956.0645-.588.0366-.3023.0803-.601.123-.9004.0459-.3023.0904-.607.1485-.9062.0213-.113.0504-.2691.084-.4004.006-.3237-.1811-.3295-.291-.3203-.1039.0091-.1803.0935-.2383.2676-.1344.4122-.414
 1.421-.5118
 2.7617-.8489-.565-1.5345-.7417-2.5117-.2988-.0672-.3146-.1213-.6489-.164-1-.1833-1.5422.0462-2.672.4218-3.4844.5803.4031
 1.3302.6326 2.0723.7578a3.7398 3.7398 0 0
 1-1.8223-1.3184zm14.8985.4825a.3674.3674 0 0 1 .2597.0976c.003 0
 .0067.0028.0098.0059.4886.4764.8402 1.0798.9043
 1.6875.0703.6993-1.0642
 1.2473-1.5742.7617-.2901-.2748-.2683-.8067-.7324-1.2617a.1822.1822 0
 0 0 .0195-.0801c.0214-.5925.4964-1.2384
 1.1133-1.211zm-4.5918.3144a1.602 1.602 0 0 0 .1972.5547 1.481 1.481 0
 0 0 .459.5039 5.1464 5.1464 0 0
 0-.1445.1309c-.1527.1496-.299.3116-.4395.4765a.2593.2593 0 0
 0-.1093-.0215c-.1772.0092-.354-.0728-.4883-.1796-.1436-.113-.3512-.3577-.336-.5684a7.122
 7.122 0 0 1 .8614-.8965zm-1.2031
 1.3496c.0984.1851.235.3476.4003.4766.1604.1277.348.215.5489.2558a9.5353
 9.5353 0 0 0-.8496 1.3809 2.3558 2.3558 0 0 0-.6094-.7344 2.1061
 2.1061 0 0 0-.2246-.1543 9.9204 9.9204 0 0 1 .7344-1.2246zM14.39
 17.012c.5925.2748.9664.9011 1.0488
 1.6035-.4794.1405-1.0044.3915-1.4472.6113.165-.6105.2864-1.2316.3633-1.8593a6.107
 6.107 0 0 0
 .0351-.3555zm-9.2617.0137c.0092.116.021.2307.0332.3437.0769.6278.1982
 1.2508.3633
 1.8614-.4367-.2169-.9485-.462-1.4219-.6055.0794-.6962.4421-1.3187
 1.0254-1.5996zm1.8965 1.666c.5202.0206 1.0323.287 1.414.621.0214
 1.472.3308 2.8553.5293
 3.127.2016.2688.0938.754.0938.754s-2.602.0671-2.8555
 0c-.2535-.0672-.555-.8145-.1367-1.2481.1954-.2015.4753-.251.7227-.248.507.1099.8366.4235
 1.1816.8632-.0733-.7543-.4965-.9515-.7988-1.1347-.0977-.058-.1356-.0859-.1875-.1836a10.8387
 10.8387 0 0 1-.8828-2.2852c.292-.2027.6077-.278.9199-.2656zm5.4687
 0c.3119-.0124.628.063.92.2656a11.035 11.035 0 0 1-.879
 2.2852c-.055.0977-.0928.1256-.1874.1836-.3024.1832-.7256.3804-.7989
 1.1347.3451-.4397.6747-.7533
 1.1817-.8632.2473-.003.5302.0465.7226.248.4184.4336.1168 1.1809-.1367
 1.248-.2535.0672-2.8555 0-2.8555
 0s-.1058-.4851.0957-.7539c.1986-.2717.51-1.655.5313-3.127.378-.334.8865-.6004
 1.4062-.621zm-8.6601.3887c.4642.1221 1.2316.477
 1.9004.828.1069.3146.226.6216.3574.924.045.1025.092.2056.1406.3066a1.4131
 1.4131 0 0 0-.621.3691 1.3835 1.3835 0 0
 0-.379.9063H2.8296c-.2413-.2016.0279-2.03
 2.3945-.9551-.5222-.4153-1.412-.9712-1.3906-2.379zm11.8496 0c.0214
 1.4077-.8676 1.9636-1.3867 2.3789 2.3636-1.075 2.6349.7535
 2.3906.955h-2.4453a1.324 1.324 0 0 0-1.0176-1.246 9.3621 9.3621 0 0 0
 .4766-1.2149c.6901-.3695 1.503-.7478 1.9824-.873zm-5.1856.412a9.7574
 9.7574 0 0 1-.1796 1.7384c-.0398.2015-.1404.689-.2442.8691a1.4439
 1.4439 0 0 0-.0781.1289c-.1487.0023-.2692.0013-.42.002a1.6751 1.6751
 0 0 0-.0956-.1582 1.8492 1.8492 0 0 1-.0977-.2754 7.2305 7.2305 0 0
 1-.1777-.793 10.22 10.22 0 0 1-.1387-1.5 4.8903 4.8903 0 0 0
 1.4316-.0117Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/cdfoundation/artwork/blob/'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/cdfoundation/artwork/blob/
3e748ca9cf9c3136a4a571f7655271b568c16a64/tekton/icon/black/tekton-icon'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
