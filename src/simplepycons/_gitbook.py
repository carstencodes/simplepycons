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


class GitbookIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gitbook"

    @property
    def original_file_name(self) -> "str":
        return "gitbook.svg"

    @property
    def title(self) -> "str":
        return "GitBook"

    @property
    def primary_color(self) -> "str":
        return "#BBDDE5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GitBook</title>
     <path d="M12.513 1.097c-.645 0-1.233.34-2.407 1.017L3.675
 5.82A7.233 7.233 0 0 0 0 12.063v.236a7.233 7.233 0 0 0 3.667
 6.238L7.69 20.86c2.354 1.36 3.531 2.042 4.824 2.042 1.292.001
 2.47-.678 4.825-2.038l4.251-2.453c1.177-.68 1.764-1.02
 2.087-1.579.323-.56.324-1.24.323-2.6v-2.63a1.04 1.04 0 0
 0-1.558-.903l-8.728 5.024c-.587.337-.88.507-1.201.507-.323
 0-.616-.168-1.204-.506l-5.904-3.393c-.297-.171-.446-.256-.565-.271a.603.603
 0 0 0-.634.368c-.045.111-.045.282-.043.625.002.252 0
 .378.025.494.053.259.189.493.387.667.089.077.198.14.416.266l6.315
 3.65c.589.34.884.51 1.207.51.324 0 .617-.17
 1.206-.509l7.74-4.469c.202-.116.302-.172.377-.13.075.044.075.16.075.392v1.193c0
 .34.001.51-.08.649-.08.14-.227.224-.522.394l-6.382
 3.685c-1.178.68-1.767 1.02-2.413 1.02-.646
 0-1.236-.34-2.412-1.022l-5.97-3.452-.043-.025a4.106 4.106 0 0
 1-2.031-3.52V11.7c0-.801.427-1.541 1.12-1.944a1.979 1.979 0 0 1
 1.982-.001l4.946 2.858c1.174.679 1.762 1.019 2.407 1.02.645 0
 1.233-.34 2.41-1.017l7.482-4.306a1.091 1.091 0 0 0 0-1.891L14.92
 2.11c-1.175-.675-1.762-1.013-2.406-1.013Z" />
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
