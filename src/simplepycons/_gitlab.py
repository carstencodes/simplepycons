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


class GitlabIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gitlab"

    @property
    def original_file_name(self) -> "str":
        return "gitlab.svg"

    @property
    def title(self) -> "str":
        return "GitLab"

    @property
    def primary_color(self) -> "str":
        return "#FC6D26"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GitLab</title>
     <path d="m23.6004 9.5927-.0337-.0862L20.3.9814a.851.851 0 0
 0-.3362-.405.8748.8748 0 0 0-.9997.0539.8748.8748 0 0
 0-.29.4399l-2.2055 6.748H7.5375l-2.2057-6.748a.8573.8573 0 0
 0-.29-.4412.8748.8748 0 0 0-.9997-.0537.8585.8585 0 0
 0-.3362.4049L.4332 9.5015l-.0325.0862a6.0657 6.0657 0 0 0 2.0119
 7.0105l.0113.0087.03.0213 4.976 3.7264 2.462 1.8633 1.4995
 1.1321a1.0085 1.0085 0 0 0 1.2197 0l1.4995-1.1321 2.4619-1.8633
 5.006-3.7489.0125-.01a6.0682 6.0682 0 0 0 2.0094-7.003z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://about.gitlab.com/handbook/marketing/c'''
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
