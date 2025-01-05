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


class ApifoxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apifox"

    @property
    def original_file_name(self) -> "str":
        return "apifox.svg"

    @property
    def title(self) -> "str":
        return "Apifox"

    @property
    def primary_color(self) -> "str":
        return "#F44A53"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apifox</title>
     <path d="M23.9747 10.0653a10.4564 10.4564 0 0 0-.456-2.3542
 4.1208 4.1208 0 0 1-.364.7432A9.4202 9.4202 0 0 0 19.306 2.19 9.3682
 9.3682 0 0 0 16.9823.9788a7.3504 7.3504 0 0 0-.3378-.1114 7.0423
 7.0423 0 0 1 1.425 3.4709c.0056.044.0106.088.015.1325a.0606.0606 0 0
 1 0 .01c.0045.0456.009.0913.0123.1375v.024a5.249 5.249 0 0 1
 .0095.1368c.0028.0457.0049.0919.0066.1375 0 .0323 0
 .0652.0033.0975a.1938.1938 0 0 0 0 .0155v.1648a7.0468 7.0468 0 0
 1-1.267 4.0414 6.3345 6.3345 0 0 1 .0746 2.1955 6.1772 6.1772 0 0 0
 1.164-.4013 6.1845 6.1845 0 0 0
 .801-.4408c.0524.182.0969.3673.132.5566.0747.3914.112.789.1114
 1.1873a6.3172 6.3172 0 0 1-.0708.9464 6.2386 6.2386 0 0 0
 1.6144-.3897c.272-.1054.5361-.23.7905-.3729.0382.213.0653.4277.0812.6435.012.1566.0178.3147.0178.4743a6.3081
 6.3081 0 0 1-.1341 1.2981 6.2523 6.2523 0 0 0 1.906-.3807 10.457
 10.457 0 0 0 .6614-3.6713 8.6007 8.6007 0 0 0-.024-.8155zm-2.8073
 5.7933a5.6853 5.6853 0 0 1-.3896.0128h-.1298a6.2501 6.2501 0 0 0
 .1977-1.5676c0-.2356-.0132-.4712-.0395-.7053a6.2298 6.2298 0 0
 1-1.9445.5945 6.0272 6.0272 0 0 1-.5723.05 6.2018 6.2018 0 0 0
 .1147-.9278 6.4769 6.4769 0 0 0 .0078-.3124 6.2899 6.2899 0 0
 0-.1414-1.332 6.2339 6.2339 0 0 1-2.1203.7759l-.0051-.0066a6.1778
 6.1778 0 0 0 .1114-.8857 5.6166 5.6166 0 0 0
 .0095-.3396c0-.3786-.034-.7564-.1019-1.1289a7.0574 7.0574 0 0
 1-5.1175 2.1877 7.043 7.043 0 0 1-3.2465-.7872 6.2634 6.2634 0 0 0
 1.2937-.6852 6.3 6.3 0 0 1-3.5727-5.6808 6.2958 6.2958 0 0 1
 .1024-1.1345 6.196 6.196 0 0 1 .3012-1.0877 6.2072 6.2072 0 0 1
 .4848-1.002 6.2628 6.2628 0 0 1 .7549-1.017 12.2123 12.2123 0 0
 0-2.6843 1.67A12.2067 12.2067 0 0 0 .3279 9.1812 12.196 12.196 0 0 0
 0 12.0013a12.1531 12.1531 0 0 0 1.4902 5.8507 6.251 6.251 0 0 1
 .4453-1.7128 11.659 11.659 0 0 0 8.5845 6.9934 6.2357 6.2357 0 0
 1-.8038-1.3833 11.008 11.008 0 0 0 3.1256.5338c.0941 0
 .1887.0033.2834.0033a10.9836 10.9836 0 0 0 4.867-1.129 6.1759 6.1759
 0 0 1-.7237-.4781 10.5065 10.5065 0 0 0 4.3203-3.0945 10.4688 10.4688
 0 0 0 1.3555-2.0925 6.2582 6.2582 0 0 1-1.7769.3662z" />
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
