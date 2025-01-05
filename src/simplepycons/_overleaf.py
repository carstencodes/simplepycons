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


class OverleafIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "overleaf"

    @property
    def original_file_name(self) -> "str":
        return "overleaf.svg"

    @property
    def title(self) -> "str":
        return "Overleaf"

    @property
    def primary_color(self) -> "str":
        return "#47A141"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Overleaf</title>
     <path d="M22.3515.7484C19.1109-.5101 7.365-.982 7.3452
 6.0266c-3.4272 2.194-5.6967 5.768-5.6967 9.598a8.373 8.373 0 0 0
 13.1225 6.898 8.373 8.373 0 0
 0-1.7668-14.7194c-.6062-.2339-1.9234-.6481-2.9753-.559-1.5007.9544-3.3308
 2.9155-4.1949 4.8693 2.5894-3.082 7.5046-2.425 9.1937 1.2287 1.6892
 3.6538-.9944 7.8237-5.0198 7.7998a5.4995 5.4995 0 0
 1-4.1949-1.9328c-1.485-1.7483-1.8678-3.6444-1.5615-5.4975
 1.057-6.4947 8.759-10.1894 14.486-11.6094-1.8677.989-5.2373
 2.6134-7.5948 4.3837C18.015 9.1382 19.1308 3.345 22.3515.7484z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.overleaf.com/for/press/media-reso'''

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
