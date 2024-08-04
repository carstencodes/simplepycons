#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class CaffeineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "caffeine"

    @property
    def original_file_name(self) -> "str":
        return "caffeine.svg"

    @property
    def title(self) -> "str":
        return "Caffeine"

    @property
    def primary_color(self) -> "str":
        return "#0000FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Caffeine</title>
     <path d="M6.162 1.557c-.18.006-.263.137-.293.18L.05
 11.82c-.07.142-.06.27-.004.356 1.942 3.36 3.882 6.723 5.822
 10.085a.337.337 0 00.305.182h11.65c.138.003.26-.09.31-.182 1.94-3.36
 3.878-6.721 5.82-10.08a.361.361 0
 000-.358l-5.82-10.085c-.112-.193-.308-.181-.308-.181zm.804.719h9.513L10.136
 5.94zm-.427.603l2.964 3.426L6.54 8.018zm10.3.018l-3.86 6.685L7.19
 8.469zm1.341.357l4.756 8.246-4.756-.916zm-12.36.002v5.176l-4.48
 2.587zm11.64 0v11.142l-3.857-4.457zM7.127 9.186l5.847 1.126 3.898
 4.502-5.842-1.125zM5.82 9.26v3.425l-4.45-.855zm.72.341l3.856
 4.457-3.857 6.685zm11.64 1.713l4.447.856-4.447 2.57zM1.062
 12.5l4.76.916v7.33zm21.597.48l-4.479 7.763v-5.175zm-11.64 1.437l5.79
 1.114-9.649 5.572zm6.44 1.565v5.138l-2.964-3.425zm-3.597 2.078l3.172
 3.664H7.52z" />
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
