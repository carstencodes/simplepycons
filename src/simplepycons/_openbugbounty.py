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


class OpenBugBountyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openbugbounty"

    @property
    def original_file_name(self) -> "str":
        return "openbugbounty.svg"

    @property
    def title(self) -> "str":
        return "Open Bug Bounty"

    @property
    def primary_color(self) -> "str":
        return "#F67909"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Open Bug Bounty</title>
     <path d="M8.092 2.443a1.388 1.388 0 0 0-1.428 1.611c.42 2.567
 2.11 4.115 3.58 4.998a14.12 14.12 0 0 0 .4 2.926H6.52a1.388 1.388 0 0
 0 0 2.777h5.155c.39.767.85 1.475 1.37 2.108-1.816 1.36-3.516
 3.734-4.34 4.983a1.388 1.388 0 1 0 2.316 1.531c1.376-2.08 3.15-4.046
 4.09-4.604a8.208 8.208 0 0 0 3.757
 1.416V6.492h-7.484c-.867-.588-1.753-1.506-1.979-2.886a1.388 1.388 0 0
 0-1.313-1.163zM18.859 0c-2.971 0-5.501 1.967-6.577 4.765h6.577Z" />
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
