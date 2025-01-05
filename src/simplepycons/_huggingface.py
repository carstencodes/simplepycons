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


class HuggingFaceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "huggingface"

    @property
    def original_file_name(self) -> "str":
        return "huggingface.svg"

    @property
    def title(self) -> "str":
        return "Hugging Face"

    @property
    def primary_color(self) -> "str":
        return "#FFD21E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hugging Face</title>
     <path d="M1.4446 11.5059c0 1.1021.1673 2.1585.4847
 3.1563-.0378-.0028-.0691-.0058-.1058-.0058-.4209
 0-.8015.16-1.0704.4512-.3454.3737-.4984.8335-.4316 1.293a1.576 1.576
 0 0 0
 .2148.5978c-.2319.1864-.4018.4456-.4844.7578-.0646.2448-.131.7543.2149
 1.2794a1.4552 1.4552 0 0 0-.0625.1055c-.208.3923-.2207.8372-.0371
 1.25.2783.6258.9696 1.1175 2.3126 1.6467.8356.3292 1.5988.5411
 1.6056.543 1.1046.2847 2.104.4277 2.969.4277 1.4173 0 2.4754-.3849
 3.1525-1.1446 1.538.2651 2.791.1403 3.592.006.6773.7555 1.7332 1.1387
 3.1467 1.1387.8649 0 1.8643-.143 2.969-.4278.0068-.0019.77-.2138
 1.6056-.543 1.343-.5292 2.0343-1.0208
 2.3126-1.6466.1836-.4129.171-.8577-.037-1.25a1.4685 1.4685 0 0
 0-.0626-.1056c.346-.525.2795-1.0346.2149-1.2793-.0826-.3122-.2525-.5714-.4844-.7579.11-.1816.1831-.3788.2148-.5977.0669-.4595-.0862-.9193-.4316-1.293-.2688-.2913-.6495-.4513-1.0704-.4513-.0209
 0-.0376.0008-.0588.0018.3162-.9966.4846-2.0518.4846-3.1523
 0-5.807-4.7362-10.5144-10.5789-10.5144-5.8426 0-10.5788
 4.7073-10.5788 10.5144Zm10.5788-9.4831c5.2727 0 9.5476 4.246 9.5476
 9.483a9.4201 9.4201 0 0 1-.2696
 2.2365c-.0039-.0047-.0079-.011-.0117-.0156-.274-.3255-.6679-.5059-1.1075-.5059-.352
 0-.714.1155-1.0763.3438-.2403.1517-.5058.422-.7793.7598-.2534-.3492-.608-.5832-1.0137-.6465a1.5174
 1.5174 0 0 0-.2344-.0176c-.9263 0-1.4828.7993-1.6935
 1.5177-.1046.2426-.6065 1.3482-1.3614 2.0978-1.1681 1.1601-1.4458
 2.3534-.8396
 3.6382-.843.1029-1.5836.0927-2.365-.006.5906-1.212.3626-2.4388-.8426-3.6322-.755-.7496-1.2568-1.8552-1.3614-2.0978-.2107-.7184-.7673-1.5177-1.6935-1.5177-.078
 0-.1568.0054-.2344.0176-.4057.0633-.7604.2973-1.0137.6465-.2735-.3379-.539-.6081-.7794-.7598-.3622-.2283-.7243-.3438-1.0762-.3438-.4266
 0-.8094.171-1.0821.4786a9.4208 9.4208 0 0 1-.2598-2.1936c0-5.237
 4.2749-9.483 9.5475-9.483zM8.6443
 7.0036c-.4838.0043-.9503.2667-1.1934.7227-.3536.6633-.1006
 1.4873.5645 1.84.351.1862.4883-.5261.836-.6485.3107-.1095.841.399
 1.0078.086.3536-.6634.1025-1.4874-.5625-1.84a1.3659 1.3659 0 0
 0-.6524-.1602Zm6.8403
 0c-.2199-.002-.4426.05-.6504.1602-.665.3526-.9181 1.1766-.5645
 1.84.1669.313.6971-.1955
 1.0079-.086.3476.1224.4867.8347.838.6485.6649-.3527.916-1.1767.5624-1.84-.243-.456-.7096-.7184-1.1934-.7227Zm-9.7565
 1.418a.8768.8768 0 0 0-.877.877c0 .4846.3925.877.877.877a.8768.8768 0
 0 0 .877-.877.8768.8768 0 0 0-.877-.877zm12.6434 0c-.4845
 0-.879.3925-.879.877 0 .4846.3945.877.879.877a.8768.8768 0 0 0
 .877-.877.8768.8768 0 0 0-.877-.877zM8.7927
 11.459c-.179-.003-.2793.1107-.2793.416 0 .8097.3874 2.125 1.4279
 2.924.207-.7123 1.3453-1.2832
 1.5079-1.2012.2315.1167.2191.4417.6074.7266.3884-.285.374-.6098.6056-.7266.1627-.082
 1.3009.4889 1.5079 1.2012 1.0404-.799 1.4278-2.1144 1.4278-2.924
 0-1.2212-1.583.6402-3.5413.6485-1.4686-.0061-2.7266-1.0558-3.2639-1.0645zM4.312
 14.4768c.5792.365 1.6964 2.2751 2.1056
 3.0177.1371.2488.371.3536.582.3536.4188 0
 .7465-.4138.0391-.9395-1.0636-.791-.6914-2.0846-.1836-2.1642a.4302.4302
 0 0 1 .0664-.004c.4616 0 .666.7892.666.7892s.5959 1.4898 1.6213
 2.508c.942.9356 1.062 1.703.4961
 2.6661-.0164-.004-.0159.0236-.1484.2149-.1853.2673-.4322.4688-.7188.6152-.5062.2269-1.1397.2696-1.7833.2696-1.037
 0-2.1017-.1824-2.6975-.336-.0293-.0075-3.6505-.9567-3.1916-1.8224.0771-.1454.2033-.2031.3633-.2031.6463
 0 1.823.9551 2.3283.9551.113 0
 .196-.0865.2285-.2031.2249-.8045-3.2787-1.0522-2.9846-2.1642.0519-.1967.193-.2757.3907-.2754.854
 0 2.7704 1.4923 3.172 1.4923.0307 0
 .0525-.0085.0645-.0274.2012-.3227.1096-.5865-1.3087-1.4395-1.4182-.8533-2.4315-1.329-1.8653-1.9416.0651-.0707.1574-.1015.2695-.1015.8611.0002
 2.8948 1.84 2.8948 1.84s.5487.5683.8809.5683c.0762 0
 .1416-.0315.1855-.1054.2355-.3946-2.1858-2.2183-2.3224-2.971-.0926-.51.0641-.7676.3555-.7676-.0006.008.1701-.0285.4942.1759zm16.2257.5918c-.1366.7526-2.5579
 2.5764-2.3224 2.9709.044.074.1092.1055.1855.1055.3321 0
 .881-.5684.881-.5684s2.0336-1.8397 2.8947-1.84c.1121 0
 .2044.0308.2695.1016.5662.6125-.447 1.0882-1.8653
 1.9415-1.4183.853-1.51 1.1168-1.3087
 1.4396.012.0188.0337.0273.0644.0273.4016 0 2.3181-1.4923
 3.1721-1.4923.1977-.0002.3388.0787.3907.2754.294 1.112-3.2095
 1.3597-2.9846 2.1642.0325.1166.1156.2032.2285.2032.5054 0 1.682-.9552
 2.3283-.9552.16 0 .2862.0577.3633.2032.459.8656-3.1623 1.8149-3.1916
 1.8224-.5958.1535-1.6605.336-2.6975.336-.6351
 0-1.261-.0409-1.7638-.2599-.2949-.1472-.5488-.3516-.7383-.625-.0411-.0682-.1026-.1476-.1426-.205-.5726-.9679-.455-1.7371.4903-2.676
 1.0254-1.0182 1.6212-2.508
 1.6212-2.508s.2044-.7891.666-.7891a.4318.4318 0 0 1
 .0665.0039c.5078.0796.88 1.3732-.1836
 2.1642-.7074.5257-.3797.9395.039.9395.211 0
 .445-.1047.5821-.3535.4092-.7426 1.5264-2.6527
 2.1056-3.0178.5588-.3524.99-.1816.8497.5918z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
