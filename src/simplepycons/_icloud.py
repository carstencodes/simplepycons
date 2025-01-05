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


class IcloudIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "icloud"

    @property
    def original_file_name(self) -> "str":
        return "icloud.svg"

    @property
    def title(self) -> "str":
        return "iCloud"

    @property
    def primary_color(self) -> "str":
        return "#3693F3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>iCloud</title>
     <path d="M13.762 4.29a6.51 6.51 0 0 0-5.669 3.332 3.571 3.571 0 0
 0-1.558-.36 3.571 3.571 0 0 0-3.516 3A4.918 4.918 0 0 0 0
 14.796a4.918 4.918 0 0 0 4.92 4.914 4.93 4.93 0 0 0
 .617-.045h14.42c2.305-.272 4.041-2.258 4.043-4.589v-.009a4.594 4.594
 0 0 0-3.727-4.508 6.51 6.51 0 0 0-6.511-6.27z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:IClou'''

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
