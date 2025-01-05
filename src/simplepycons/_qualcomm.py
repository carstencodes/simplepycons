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


class QualcommIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qualcomm"

    @property
    def original_file_name(self) -> "str":
        return "qualcomm.svg"

    @property
    def title(self) -> "str":
        return "Qualcomm"

    @property
    def primary_color(self) -> "str":
        return "#3253DC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qualcomm</title>
     <path d="M12 0C6.22933 0 1.5761 4.48645 1.5761 10.47394c0 6.00417
 4.65323 10.47394 10.4239 10.47394.98402 0 1.93468-.13343
 2.8353-.3836l1.13412
 2.9187c.11675.31688.35025.51702.7672.51702h1.80125c.43364 0
 .75052-.28353.55038-.83391l-1.46768-3.81932c2.88534-1.81793
 4.80333-5.03683 4.80333-8.8895C22.4239 4.48644 17.77067 0 12
 0m4.53648
 16.5615l-1.31758-3.41904c-.11675-.28353-.35024-.55038-.85059-.55038h-1.71786c-.43363
 0-.7672.28353-.56706.83391l1.73454
 4.48645c-.56706.1501-1.18416.21682-1.81793.21682-4.2196
 0-7.22168-3.31897-7.22168-7.65532C4.77832 6.1376 7.7804 2.81862 12
 2.81862s7.22168 3.31898 7.22168 7.65532c0 2.5351-1.01737
 4.70327-2.6852 6.08756" />
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
