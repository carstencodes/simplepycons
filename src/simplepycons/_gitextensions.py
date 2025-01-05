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


class GitExtensionsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gitextensions"

    @property
    def original_file_name(self) -> "str":
        return "gitextensions.svg"

    @property
    def title(self) -> "str":
        return "Git Extensions"

    @property
    def primary_color(self) -> "str":
        return "#212121"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Git Extensions</title>
     <path d="M17.504 0l-4.631 4.875 2.533.004c0 2.604-1.327 4.58-3.32
 6.16l-6.393 5.065c-2.559 2.027-3.859 4.392-3.859 7.886.01-.009
 4.283.026 4.283 0 0-1.91.73-3.581 2.223-4.793l6.723-5.455c2.57-2.085
 4.514-4.86 4.517-8.867h2.586zM1.834 4.873c0 3.78 1.833 6.398 4.148
 8.518l1.11.88 3.222-2.554-1.078-.858C7.43 9.22 6.117 7.383 6.117
 4.873c-1.423-.004-2.856 0-4.283 0zm12.592 10.115l-3.178
 2.58.992.787c1.82 1.593 3.166 3.33 3.166
 5.635h4.166c-.009-3.633-1.788-6.1-4.066-8.144-.356-.28-.722-.572-1.08-.858Z"
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
        return '''https://github.com/gitextensions/gitextension
s/blob/273a0f6fd3e07858f837cdc19d50827871e32319/Logo/Artwork/git-exten'''

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
