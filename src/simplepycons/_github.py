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


class GithubIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "github"

    @property
    def original_file_name(self) -> "str":
        return "github.svg"

    @property
    def title(self) -> "str":
        return "GitHub"

    @property
    def primary_color(self) -> "str":
        return "#181717"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GitHub</title>
     <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205
 11.385.6.113.82-.258.82-.577
 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07
 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838
 1.236 1.838 1.236 1.07 1.835 2.809 1.305
 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93
 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0
 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405
 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84
 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81
 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092
 24 17.592 24 12.297c0-6.627-5.373-12-12-12" />
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
