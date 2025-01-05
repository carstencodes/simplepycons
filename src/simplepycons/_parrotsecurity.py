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


class ParrotSecurityIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "parrotsecurity"

    @property
    def original_file_name(self) -> "str":
        return "parrotsecurity.svg"

    @property
    def title(self) -> "str":
        return "Parrot Security"

    @property
    def primary_color(self) -> "str":
        return "#15E0ED"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Parrot Security</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0Zm6.267 2.784L13.03 5.54l8.05-.179-8.05
 3.333-2.154 2.688 5.007 9.038-1.536-1.605 1.645
 3.456-4.937-5.527-6.268-6.28L2.77 12.11l.7-3.442
 4.018-.261.823-4.06Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://gitlab.com/parrotsec/project/document
ation/-/blob/d1d426b9cb3ea0efd16a2b34056c1ebb21bb9af9/static/img/parro'''

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
