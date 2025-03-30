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


class GleamIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gleam"

    @property
    def original_file_name(self) -> "str":
        return "gleam.svg"

    @property
    def title(self) -> "str":
        return "Gleam"

    @property
    def primary_color(self) -> "str":
        return "#FFAFF3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gleam</title>
     <path d="M10.6144.0026a1.9 1.9 0 0
 0-.229.0261l.0001.0002C9.78.1358 9.2263.538 8.9971 1.1873l-1.7855
 5.059A1.8 1.8 0 0 1 6.1704 7.323L1.1706 9.282c-1.283.5027-1.531
 2.2673-.4373 3.1027l4.2646 3.257a1.795 1.795 0 0 1 .7031 1.3212l.3179
 5.3537c.0815 1.3735 1.6836 2.1548 2.819
 1.3729v-.0002l4.4212-3.0459v-.0001a1.8 1.8 0 0 1 1.4757-.2601l5.1962
 1.3498c1.3342.3467 2.5725-.9356
 2.1794-2.2543v.0002l-1.532-5.1397a1.796 1.796 0 0 1
 .209-1.482v-.0002l2.8934-4.5194c.742-1.1591-.0945-2.7324-1.472-2.766l-5.368-.1303a1.8
 1.8 0 0
 1-1.3467-.6558L12.0862.6422c-.3827-.4654-.9342-.6678-1.4718-.6396m5.7066
 10.4086c.4626-.0106.8762.3176.959.7872a.953.953 0 0 1-.773
 1.1038.9528.9528 0 1 1-.186-1.891M8.6439 11.765a.953.953 0 0 1
 .959.7873c.0913.5182-.2548 1.0123-.773
 1.1038s-1.0125-.2547-1.1038-.7729c-.0914-.5182.2547-1.0124.773-1.1038a.96.96
 0 0 1 .1448-.0144m4.928 1.3841a.486.486 0 0 1 .3397.15.485.485 0 0 1
 .1339.3463 1.264 1.264 0 0 1-.3917.8853v.0001h-.0002a1.266 1.266 0 0
 1-.9026.3488h-.0004a1.26 1.26 0 0 1-.4812-.1079 1.26 1.26 0 0
 1-.4038-.284 1.27 1.27 0 0 1-.2642-.4168.485.485 0 0 1
 .278-.6272.483.483 0 0 1 .371.009.485.485 0 0 1 .2561.2687.29.29 0 0
 0 .0615.097v.0002a.3.3 0 0 0 .0938.0658v.0001h.0003a.295.295 0 0 0
 .2252.0055l.0003-.0001a.292.292 0 0 0
 .1628-.1553l.0002-.0002v-.0001a.29.29 0 0 0 .025-.1116.486.486 0 0 1
 .15-.3395.485.485 0 0 1 .3463-.134z" />
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
