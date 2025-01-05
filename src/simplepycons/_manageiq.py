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


class ManageiqIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "manageiq"

    @property
    def original_file_name(self) -> "str":
        return "manageiq.svg"

    @property
    def title(self) -> "str":
        return "ManageIQ"

    @property
    def primary_color(self) -> "str":
        return "#EF2929"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ManageIQ</title>
     <path d="M12.095.1C5.718.094.544 5.26.538 11.637v.022c0 2.069.547
 4.005 1.496 5.683l2.869-2.868a7.685 7.685 0 0 1-.54-2.815c0-4.262
 3.47-7.73 7.732-7.73s7.732 3.468 7.732 7.73-3.47 7.732-7.732
 7.732a7.685 7.685 0 0 1-2.6-.46L6.596 21.83a11.515 11.515 0 0 0 5.499
 1.388c2.316 0 4.467-.686 6.275-1.856l2.393 2.392L24
 20.512l-2.349-2.349c1.262-1.852 2-4.09 2-6.505C23.66 5.269 18.452.078
 12.096.101L12.095.1zm0 9.34c-1.225 0-2.214.991-2.214 2.217s.989 2.215
 2.214 2.215a2.216 2.216 0 1 0 0-4.432zm-4.24 3.368C7.57 13.09.273
 20.39 0 20.662L3.24 23.9l7.855-7.855-3.24-3.238v.001z" />
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
