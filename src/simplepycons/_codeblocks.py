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


class CodeblocksIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codeblocks"

    @property
    def original_file_name(self) -> "str":
        return "codeblocks.svg"

    @property
    def title(self) -> "str":
        return "Code::Blocks"

    @property
    def primary_color(self) -> "str":
        return "#41AD48"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Code::Blocks</title>
     <path d="M.011 0v8.406H8.61V0zm15.39 0v8.406H24V0zM8.972.658l.012
 7.869 2.54 2.43.007-5.564zm6.066 0-2.555 4.735.004 5.564
 2.54-2.43zM.332 8.768l5.52 2.677 5.655-.006-2.773-2.67zm14.944
 0L12.53 11.49l5.655-.09 5.498-2.631zm-9.323 3.855L.318
 15.232h8.405l2.748-2.722zm6.565-.113 2.747
 2.722h8.402l-5.586-2.609zm-1.006.533-2.54 2.43-.011 7.873
 2.555-4.74zm.964 0-.008 5.564 2.559 4.74-.011-7.874zM0
 15.598V24h8.598v-8.402zm15.39 0V24h8.598v-8.402z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://wiki.codeblocks.org/index.php/Main_Pa'''

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
