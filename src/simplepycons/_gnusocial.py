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


class GnuSocialIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gnusocial"

    @property
    def original_file_name(self) -> "str":
        return "gnusocial.svg"

    @property
    def title(self) -> "str":
        return "GNU social"

    @property
    def primary_color(self) -> "str":
        return "#A22430"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GNU social</title>
     <path d="M4.217 0C2.474 0 1.06 1.413 1.06 3.156V15.77c0 1.744
 1.414 3.158 3.157 3.158h9.367C13.567 22.498 8.756 24 8.756
 24s8.138-.038 9.305-5.072h1.72c1.744 0 3.157-1.414
 3.157-3.157V3.157C22.938 1.413 21.524 0 19.782 0H4.218zm4.527
 2.53c.073-.013.132-.003.174.034.335.3-.556.593-.484 2.063.032.646-.16
 1.146 1.076 1.146.826 0 .483-.734 1.523-.734.656 0
 .86.435.934.767.072-.33.274-.768.93-.768 1.04 0 .7.733 1.525.733
 1.237 0 1.044-.5
 1.076-1.146.072-1.47-.82-1.764-.484-2.063.042-.037.1-.042.172-.02.5.143
 1.607 1.558 1.638 2.155.038.71.04 1.825-1.015 2.407 1.19 1.167 1.352
 2.72 1.352
 2.72l-2.045-.034s-.464-2.118-2.94-2.01c-2.474.108-2.796.538-2.796
 3.156 0 2.617 1.147 3.517 2.905 3.585 2.76.108 2.51-1.433
 2.51-1.433l-1.29.072-.718-1.937h4.41c0 2.116-.897 5.414-5.092
 5.2-4.196-.216-5.128-3.515-5.164-5.74-.018-1.225.188-2.602
 1.2-3.574-1.052-.58-1.033-1.7-1.033-2.414 0-.88 1.13-2.084
 1.637-2.17z" />
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
