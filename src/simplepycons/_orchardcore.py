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


class OrchardCoreIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "orchardcore"

    @property
    def original_file_name(self) -> "str":
        return "orchardcore.svg"

    @property
    def title(self) -> "str":
        return "Orchard Core"

    @property
    def primary_color(self) -> "str":
        return "#41B670"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Orchard Core</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.629 0 12 0m0 21.69c-5.352 0-9.692-4.338-9.692-9.692 0-5.352
 4.338-9.691 9.692-9.691 5.352 0 9.692 4.338 9.692 9.691A9.69 9.69 0 0
 1 12 21.69m5.778-3.964a7.996 7.996 0 0 1 0-11.305 7.993 7.993 0 0 1 0
 11.305m-3.212-3.211A7.994 7.994 0 0 1 6.572 6.52a7.996 7.996 0 0 1
 7.994 7.994m-8.13 3.242a7.996 7.996 0 0 1 11.306 0 7.996 7.996 0 0
 1-11.305 0" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://docs.orchardcore.net/en/latest/refere'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://docs.orchardcore.net/en/latest/refere
nce/branding/assets/logo/symbol/color/orchard-core-symbol-logo-color.s'''

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
