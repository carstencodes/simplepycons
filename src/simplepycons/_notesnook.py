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


class NotesnookIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "notesnook"

    @property
    def original_file_name(self) -> "str":
        return "notesnook.svg"

    @property
    def title(self) -> "str":
        return "Notesnook"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Notesnook</title>
     <path d="M7.2 0C3.21 0 0 3.21 0 7.2v9.6C0 20.79 3.21 24 7.2
 24h9.6c3.99 0 7.2-3.21 7.2-7.2V7.2C24 3.21 20.79 0 16.8 0ZM6.036
 3.438H12a5.965 5.965 0 0 1 5.963 5.964c-.003 1.8.005 3.598-.004
 5.397l-2.094-.875V9.402a3.868 3.868 0 0 0-3.713-3.863 3.866 3.866 0 0
 0-2.718.973 3.866 3.866 0 0 0-1.29 2.584c-.02.532-.01 1.065-.01
 1.597l-2.097-.877Zm0 8.238 2.098.877v2.043c0 .55.116 1.096.344
 1.597a3.875 3.875 0 0 0 3.353 2.266c.027.005.188 0 .334 0a3.876 3.876
 0 0 0 3.533-2.744l1.946.814a5.962 5.962 0 0 1-6.622 3.951 5.966 5.966
 0 0 1-4.986-5.882Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/streetwriters/notesnook/bl
ob/20bbb6dd5b8d9fa0b3924f20d315babe0e3f6173/apps/web/public/favicon.sv'''

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
