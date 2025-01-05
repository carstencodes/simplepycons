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


class TinaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tina"

    @property
    def original_file_name(self) -> "str":
        return "tina.svg"

    @property
    def title(self) -> "str":
        return "Tina"

    @property
    def primary_color(self) -> "str":
        return "#EC4815"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tina</title>
     <path d="M 14.46 10.662 C 15.626 9.697 16.143 3.996 16.648 1.947
 C 17.153 -0.103 19.241 0.001 19.241 0.001 C 19.241 0.001 18.699 0.945
 18.92 1.649 C 19.141 2.353 20.656 2.982 20.656 2.982 L 20.329 3.843 C
 20.329 3.843 19.647 3.756 19.241 4.568 C 18.835 5.38 19.502 13.421
 19.502 13.421 C 19.502 13.421 17.062 18.234 17.062 20.266 C 17.062
 22.298 18.024 24 18.024 24 L 16.674 24 C 16.674 24 14.694 21.644
 14.288 20.467 C 13.882 19.289 14.045 18.112 14.045 18.112 C 14.045
 18.112 11.893 17.99 9.984 18.112 C 8.076 18.234 6.803 19.874 6.574
 20.792 C 6.344 21.709 6.249 24 6.249 24 L 5.182 24 C 4.532 21.996
 4.016 21.278 4.296 20.266 C 5.072 17.462 4.919 15.872 4.74 15.164 C
 4.56 14.456 3.345 13.838 3.345 13.838 C 3.94 12.625 4.548 12.042
 7.162 11.981 C 9.775 11.921 13.294 11.627 14.46 10.662 Z M 9.277
 18.871 C 9.277 18.871 9.413 22.579 10.669 24 L 9.413 24 C 7.949 22.7
 7.673 20.148 7.673 20.148 C 7.754 19.824 8.638 19.079 9.277 18.871 Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/tinacms/tinacms/blob/965ed
fb7d2a318ab6b86a4772e4daebf53f34f2e/examples/tina-self-hosted-demo/pub'''

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
