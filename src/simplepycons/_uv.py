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


class UvIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "uv"

    @property
    def original_file_name(self) -> "str":
        return "uv.svg"

    @property
    def title(self) -> "str":
        return "uv"

    @property
    def primary_color(self) -> "str":
        return "#DE5FE9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>uv</title>
     <path d="m0 .1058.0504 11.9496.0403 9.5597c.0055 1.3199 1.08
 2.3854 2.4 2.3798l9.5596-.0403 5.9749-.0252.6075-.0026c1.316-.0056
 2.3799-1.0963 2.3799-2.4123h1.0946v2.3894L24 23.9042 23.8992.005
 12.9056.0513l.0463 9.5245v5.9637h-1.9583L11.04 9.584 10.9936.0594Z"
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
