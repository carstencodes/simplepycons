#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class AwaitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "await"

    @property
    def original_file_name(self) -> "str":
        return "await.svg"

    @property
    def title(self) -> "str":
        return "Await"

    @property
    def primary_color(self) -> "str":
        return "#7858F5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Await</title>
     <path d="M12 0c5.523 0 10 4.477 10 10v9a3.125 3.125 0 0 1-4.694
 2.703A3.126 3.126 0 0 1 12 23a3.126 3.126 0 0 1-5.306-1.297A3.125
 3.125 0 0 1 2 19v-9C2 4.477 6.477 0 12 0m-1.25 10.625a.625.625 0 0
 0-.625.625 1.875 1.875 0 0 0 3.75 0 .625.625 0 0
 0-.625-.625zm-1.875-5c-.69 0-1.25.56-1.25 1.25v1.25a1.25 1.25 0 0 0
 2.5 0v-1.25c0-.69-.56-1.25-1.25-1.25m6.25 0c-.69 0-1.25.56-1.25
 1.25v1.25a1.25 1.25 0 0 0 2.5 0v-1.25c0-.69-.56-1.25-1.25-1.25" />
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
