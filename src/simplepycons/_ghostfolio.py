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


class GhostfolioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ghostfolio"

    @property
    def original_file_name(self) -> "str":
        return "ghostfolio.svg"

    @property
    def title(self) -> "str":
        return "Ghostfolio"

    @property
    def primary_color(self) -> "str":
        return "#36CFCC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ghostfolio</title>
     <path d="M11.983 0a9.375 9.375 0 0 0-9.358 9.375v13.062a.781.781
 0 0 0 1.334.553l1.791-1.844 2.573 2.625c.305.305.8.305 1.105 0L12
 21.146l2.573 2.625c.305.305.8.305 1.105 0l2.572-2.625 1.792
 1.844a.781.781 0 0 0
 1.333-.553V9.455c0-5.166-4.226-9.464-9.392-9.455m-3.89 12.5a2.346
 2.346 0 0 1-2.343-2.344 2.346 2.346 0 0 1 2.344-2.344 2.346 2.346 0 0
 1 2.344 2.344A2.346 2.346 0 0 1 8.094 12.5m7.814 0a2.346 2.346 0 0
 1-2.344-2.344 2.346 2.346 0 0 1 2.344-2.344 2.346 2.346 0 0 1 2.343
 2.344 2.346 2.346 0 0 1-2.343 2.344" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/ghostfolio/ghostfolio/blob
/cc92ecf62a014b27146338bb7a20ed6eeb525fba/apps/client/src/assets/ghost'''

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
