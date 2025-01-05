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


class QiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qi"

    @property
    def original_file_name(self) -> "str":
        return "qi.svg"

    @property
    def title(self) -> "str":
        return "Qi"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qi</title>
     <path d="M16.5742 0c-.8422 0-1.525.6826-1.525 1.5247 0 .8424.6828
 1.525 1.525 1.525s1.5247-.6826 1.5247-1.525C18.0989.6826 17.4164 0
 16.5742 0zm-4.6371 2.856c-1.7103.0124-3.4264.5973-4.8392
 1.7828-3.2263 2.7071-3.6471 7.5175-.94 10.7439 1.4616 1.7419 3.5365
 2.6653 5.6439 2.7208.2966 0 .2966.293.2966.293v2.65s.0002 2.7624
 2.6567
 2.9532c.2952.0103.2953-.295.2953-.295V3.7857s0-.2943-.295-.415a7.665
 7.665 0 0 0-2.8183-.5147zm4.7479
 1.662c-.1097-.0016-.1097.1789-.1097.3891v11.1466c0 .2941 0
 .5266.2948.2954.0104-.009.0211-.0175.0318-.0266 3.2265-2.707
 3.6474-7.5175.94-10.7437a7.5925 7.5925 0 0
 0-.9713-.9659c-.083-.0656-.1427-.0941-.1856-.0948zm-4.7515
 1.3885c.165 0 .165.1642.165.1642v8.8198s0
 .1644-.165.1644c-1.2823-.0192-2.5496-.5735-3.4386-1.633-1.6245-1.936-1.3719-4.8217.5639-6.4464.8395-.7046
 1.8582-1.0549 2.8747-1.069z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.wirelesspowerconsortium.com/knowl'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.wirelesspowerconsortium.com/knowl'''

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
