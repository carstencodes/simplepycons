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


class OpenverseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openverse"

    @property
    def original_file_name(self) -> "str":
        return "openverse.svg"

    @property
    def title(self) -> "str":
        return "Openverse"

    @property
    def primary_color(self) -> "str":
        return "#FFE033"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Openverse</title>
     <path d="M4.882 1.018C2.182 1.018 0 3.214 0 5.932c0 2.704 2.182
 4.915 4.882 4.915Zm7.118 0c-2.686 0-4.882 2.196-4.882 4.914 0 2.704
 2.182 4.915 4.882 4.915zm7.118 0c-2.696 0-4.881 2.2-4.881 4.914 0
 2.714 2.185 4.915 4.88 4.915 2.697 0 4.883-2.2 4.883-4.915
 0-2.714-2.186-4.914-4.882-4.914zm0 12.093c-2.696 0-4.881 2.2-4.881
 4.915 0 2.714 2.185 4.914 4.88 4.914 2.697 0 4.883-2.2 4.883-4.914
 0-2.714-2.186-4.915-4.882-4.915ZM12 13.126c-2.686 0-4.882 2.196-4.882
 4.9S9.3 22.94 12 22.94zm-7.118.04c-2.7 0-4.882 2.197-4.882 4.9 0
 2.719 2.182 4.916 4.882 4.916Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.figma.com/file/GIIQ4sDbaToCfFQyKM'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/WordPress/openverse/blob/5'''

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
