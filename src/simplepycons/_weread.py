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


class WereadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "weread"

    @property
    def original_file_name(self) -> "str":
        return "weread.svg"

    @property
    def title(self) -> "str":
        return "WeRead"

    @property
    def primary_color(self) -> "str":
        return "#37A7FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WeRead</title>
     <path d="M5.12 0A5.11 5.11 0 0 0 0 5.12v13.76A5.11 5.11 0 0 0
 5.12 24h13.76A5.11 5.11 0 0 0 24 18.88V5.12A5.11 5.11 0 0 0 18.88
 0Zm12.954 10.24c2.04 0 3.694 1.39 3.694 3.107 0 1.716-1.653
 3.107-3.694 3.107-.43 0-.842-.063-1.226-.177a.37.37 0 0
 0-.29.032l-.794.463a.123.123 0 0 1-.18-.14l.177-.668a.25.25 0 0
 0-.098-.267c-.785-.57-1.284-1.41-1.284-2.35 0-1.716 1.655-3.107
 3.695-3.107m-1.231 1.616a.495.495 0 0 0-.493.497c0
 .274.22.497.493.497a.495.495 0 0 0 .492-.497.495.495 0 0
 0-.492-.497m2.462 0a.495.495 0 0 0-.492.497c0
 .274.22.497.492.497a.495.495 0 0 0 .493-.497.495.495 0 0
 0-.493-.497M18.08 18.88h5.12c0 2.4-1.92 4.32-4.32 4.32H5.12C2.72
 23.2.8 21.28.8 18.88h5.12c1.6 0 3.914-.012 5.28 1.28.489.462.677
 1.17.798 1.17.12 0 .292-.671.802-1.17 1.305-1.275 3.215-1.28
 5.28-1.28" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://cdn.weread.qq.com/web/wrwebnjlogic/im'''

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
